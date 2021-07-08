    import kivy
    from kivy.app import App
    from kivy.uix.button import Button
    
    class ButtonApp(App):
        def build(self):
            # Make a variable for the Button class being called from Kivy
            button = Button(text="Hello World!",
                background_color=(0,0,1,1)
            )
            return button
            
     if __name__ == '__main__':
        ButtonApp().run()
