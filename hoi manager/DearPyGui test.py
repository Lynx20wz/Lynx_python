import dearpygui.demo as demo
import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title='Demo')
demo.show_demo()
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
