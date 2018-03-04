import Vue from 'vue'
import Router from 'vue-router'
import InputTable from '@/components/InputTable'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'InputTable',
      component: InputTable
    }
  ]
})
