
class SweetAlertMessage:
    def __init__(self,title,message,icon):
        self.title = title
        self.message = message,
        self.icon = icon

    def getAlert(self):
        alert = {
            "title":self.title,
            "message":self.message,
            "icon":self.icon
        }
        return alert
