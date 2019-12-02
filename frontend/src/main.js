import page from 'page'
import Vue from 'vue'
import Home from './components/Home.vue'
import SearchList from './components/SearchList.vue'

Vue.config.productionTip = false

const app = new Vue({
  el: '#app',
  data: {
    ViewComponent: { render: h => h('div', 'loading...') }
  },
  render (h) {
    return h(this.ViewComponent)
  }
})

page('/', () => app.ViewComponent = Home)
page('/search', () => app.ViewComponent = SearchList)
page()