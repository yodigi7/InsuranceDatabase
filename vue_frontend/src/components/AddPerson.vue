<template>
  <div class="container">
    <FlashMessage v-bind:message="message" type="success"></FlashMessage>
    <form @submit.prevent="addPerson">
      <fieldset class="form-group">
        <legend class="border-bottom mb-4">Add a Person</legend>
        <div class="row">
          <Person ref="person"></Person>
        </div>
      </fieldset>
      <div class="form-group float-left">
        <button class="btn btn-info">Submit</button>
      </div>
    </form>
  </div>
</template>

<script>
import Person from './Person'
import FlashMessage from './FlashMessage'
export default {
  name: 'AddPerson',
  components: {Person, FlashMessage},
  data () {
    return {
      message: null
    }
  },
  methods: {
    addPerson () {
      this.$refs.person.add()
      this.message = 'Successfully added person'
      setTimeout(() => {
        this.message = null
        console.log(this.message)
      }, 5000)
    }
  }
}
</script>

<style scoped>

</style>
