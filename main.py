from nicegui import ui

@ui.page('/')
def index():
    ui.label('Hello, NiceGUI!')
    ui.button('Click',on_click=lambda:ui.notify('It is working!',type='positive',position='center'))

ui.run(host='0.0.0.0', port=8080, reload=False)
