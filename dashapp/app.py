from dash import Dash
import dash_bootstrap_components as dbc


# สร้างอินสแตนซ์ของแอป
app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

# สามารถตั้งค่าบางอย่างเพิ่มเติมได้ที่นี่
app.config.suppress_callback_exceptions = True

if __name__ == "__main__":
    from layout import layout
    from callbacks import register_callbacks

    app.layout = layout
    register_callbacks(app)

    app.run_server(debug=True)
