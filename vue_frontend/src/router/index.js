import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import AddPerson from '@/components/AddPerson'
import ModifyPerson from '@/components/ModifyPerson'
import ListPeople from '@/components/ListPeople'
import ListOfPeople from '@/components/ListOfPeople'

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
    },
    {
      path: '/list-people/:page',
      name: 'ListPeople',
      component: ListPeople
    },
    {
      path: '/list-of-people/:ids',
      name: 'ListOfPeople',
      component: ListOfPeople,
      props (route) {
        const ids = route.params.ids || ''
        console.log(ids.split(','))
        return {
          ids: ids === '' ? [] : ids.split(',')
        }
      }
    }
  ]
})
