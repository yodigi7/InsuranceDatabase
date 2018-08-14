import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import AddPerson from '@/components/AddPerson'
import ModifyPerson from '@/components/ModifyPerson'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/add-person',
      name: 'AddPerson',
      component: AddPerson
    },
    {
      path: '/modify-person/:id',
      name: 'ModifyPerson',
      component: ModifyPerson
    }
  ]
})
