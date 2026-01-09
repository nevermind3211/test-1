from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def render(self):
        pass

class Checkbox(ABC):
    @abstractmethod
    def render(self):
        pass

class WindowsButton(Button):
    def render(self):
        return "[Windows Button]"

class WindowsCheckbox(Checkbox):
    def render(self):
        return "[Windows Checkbox] ✓"

class MacButton(Button):
    def render(self):
        return "[Mac Button]"

class MacCheckbox(Checkbox):
    def render(self):
        return "[Mac Checkbox] ✅"

class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass
    
    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass

class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()
    
    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()

class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()
    
    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()

class Application:
    def __init__(self, factory: GUIFactory):
        self.factory = factory
        self.button = None
        self.checkbox = None
    
    def create_ui(self):
        self.button = self.factory.create_button()
        self.checkbox = self.factory.create_checkbox()
    
    def render(self):
        print(f"Кнопка: {self.button.render()}")
        print(f"Чекбокс: {self.checkbox.render()}")

if __name__ == "__main__":
    config = "windows"
    
    if config == "windows":
        factory = WindowsFactory()
    else:
        factory = MacFactory()
    
    app = Application(factory)
    app.create_ui()
    app.render()
