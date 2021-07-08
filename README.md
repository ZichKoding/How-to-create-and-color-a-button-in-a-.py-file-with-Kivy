# **How to create and color a button in a .py file with Kivy**

Today we will make a button with Kivy and learn how to change its color. Before we start, remember to use the virtual environment to play with the Kivy module to prevent any mishaps with other modules.

Alright, it's time to get down to some coding. First, we will start off with making a simple button.

Input:

    import kivy
    from kivy.app import App
    from kivy.uix.button import Button
    
    class ButtonApp(App)
        def build(self):
            # Make a variable for the Button Class being called from Kivy
            button = Button(text="Hello World!")
            return button
            
    if __name__ == '__main__':
        ButtonApp().run()
        

Output:

https://www.educative.io/cdn-cgi/image/f=auto,fit=contain,w=1200/api/edpresso/shot/5896126035656704/image/4554287152103424.png

This is a button that does nothing once it's pressed, but it's okay because we are more worried about the design parts of this app than the logic. The next part is going to show how to change the color. So, what we need to do is in our variable, button, we need to go into the `Button()` method and add the keyword argument `background_color`.

It is pretty simple to make sense out of this color system. This color system is based on RGB values, so to set the color to blue would be `background_color = (0, 0, 1, 1). To understand what is going on, the tuple stands for (Red, Green, Blue, Opacity) and the 0's stand for 0% (or 0/255) while the 1's stand for 100% (or 255/255). The last value in the tuple (1) stands for opacity, which is also percentage-based.

Input: 

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
        
        
Output:

https://www.educative.io/cdn-cgi/image/f=auto,fit=contain,w=1200/api/edpresso/shot/5896126035656704/image/6211737093668864.png

Alright, we have a blue button! If you wanted a different shade of blue, you can always refer to an HTML color picker off of Google and divide each RGB value by 255. For instance, if we wanted a pink button the code would be `background_color=(255/255, 19/255, 230/255, 1).

Another way of creating and coloring a button using the Kivy design language is by making a .kv file, but I will cover that in a different shot. For now, this will be enough for creating and changing the color of a button in a .py file with Kivy.
