import Vue.Vue as Vue
import Modele.model as Model

class Controller:

    def __init__(self, model, vue):
        self.model = model
        self.vue = vue

        self.vue.