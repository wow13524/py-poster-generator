from .api.expression import Expression, ExpressionType, RawExpression
from .api.plugin import Plugin, PluginType
from importlib import import_module
from typing import Any, Dict, List

class ActiveContext:
    def __init__(self, plugins: List[Plugin], expression_map: Dict[ExpressionType, Plugin]) -> None:
        self._contexts: Dict[PluginType, Any] = {plugin.__class__: plugin.context() for plugin in plugins}
        self._expression_map = expression_map

    def evaluate_expression(self, expression: Expression) -> Any:
        kwargs: Dict[str, Any] = {}
        if expression.requires_context():
            kwargs["context"] = self._contexts[self._expression_map[expression.__class__].__class__]
        for key, subexpr in expression.children.items():
            kwargs[key] = self.evaluate_expression(subexpr)
        return expression.evaluate(**kwargs)
    
    def set_context(self, plugin_class: PluginType, context: Any) -> None:
        self._contexts[plugin_class] = context

class PluginContext:
    _CACHED_PLUGINS: Dict[PluginType, Plugin] = {}
    _DEFAULT_REQUIRED: List[str] = [
        "base"
    ]

    @staticmethod
    def _get_plugins(plugin_name: str) -> List[Plugin]:
        module: Any = import_module(plugin_name)
        plugins: List[PluginType] = getattr(module, "export_plugins")
        assert type(plugins) == list, f"{plugin_name} missing list 'export_plugins'"
        for plugin in plugins:
            assert issubclass(plugin,Plugin), f"{plugin_name} is not a subclass of Plugin"
            if plugin not in PluginContext._CACHED_PLUGINS:
                PluginContext._CACHED_PLUGINS[plugin] = plugin()
        return [PluginContext._CACHED_PLUGINS[plugin] for plugin in plugins]

    def __init__(self, plugin_list: List[str]) -> None:
        self._action_map: Dict[str,ExpressionType] = {}
        self._expression_map: Dict[ExpressionType, Plugin] = {}
        self._plugins: List[Plugin] = [
            plugin for plugin_name in PluginContext._DEFAULT_REQUIRED+plugin_list
            for plugin in PluginContext._get_plugins(plugin_name)
        ]
        
        for plugin in self._plugins:
            self._action_map.update({f"{plugin.__class__.__name__}.{expression.__qualname__}": expression for expression in plugin.expressions})
            plugin_class: PluginType = plugin.__class__
            for expression in plugin_class.expressions:
                assert expression not in self._expression_map, f"expression {expression.__name__} belongs to both {self._expression_map[expression].__class__.__name__} and {plugin_class.__name__}"
                self._expression_map[expression] = plugin
    
    def active_context(self) -> ActiveContext:
        return ActiveContext(self._plugins, self._expression_map)
    
    def parse_expression(self, raw_expression: RawExpression) -> Expression:
        try:
            expression_class: ExpressionType = self._action_map[raw_expression.action]
        except:
            raise Exception(f"expression action {raw_expression.action} does not exist")
        
        parsed_children: Dict[str, Expression] = {}
        for key in expression_class.annotations():
            try:
                parsed_children[key] = self.parse_expression(RawExpression(raw_expression.raw[key]))
            except:
                raise Exception(f"Failed to parse {key} in {raw_expression.raw}")

        return expression_class(raw_expression.raw, parsed_children)