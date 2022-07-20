import { createApp } from 'vue'
import { createPinia } from 'pinia'

import FomanticUI from 'vue-fomantic-ui'
import 'fomantic-ui-css/semantic.min.css'

import App from './App.vue'
import router from './router'

const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(FomanticUI)

app.mount('#app')
