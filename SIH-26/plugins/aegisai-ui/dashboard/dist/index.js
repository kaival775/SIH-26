(function () {
  "use strict";

  const SDK = window.__HERMES_PLUGIN_SDK__;
  const { React } = SDK;
  const { Card, CardHeader, CardTitle, CardContent } = SDK.components;

  function AegisAIPage() {
    return React.createElement(
      Card,
      null,
      React.createElement(
        CardHeader,
        null,
        React.createElement(
          CardTitle,
          null,
          "AegisAI — Sovereign Intelligence Workbench"
        )
      ),
      React.createElement(
        CardContent,
        null,
        React.createElement(
          "p",
          { className: "text-sm text-muted-foreground" },
          "AegisAI dashboard plugin loaded successfully."
        )
      )
    );
  }

  window.__HERMES_PLUGINS__.register("aegisai-ui", AegisAIPage);
})();
