<template>
  <div class="container">
    <FlashMessage v-bind:message="message" type="success"></FlashMessage>
    <form @submit.prevent="addPersonAndNote">
      <fieldset class="form-group">
        <legend class="border-bottom mb-4">Add a Person</legend>
          <Person ref="person"></Person>
          <Note ref="note"></Note>
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
import Note from './Note'
export default {
  name: 'AddPerson',
  components: {Person, FlashMessage, Note},
  data () {
    return {
      message: null
    }
  },
  methods: {
    addPersonAndNote () {
      this.$refs.person.add()
        .then((uniqueId) => {
          console.log(uniqueId)
          this.$refs.note.add(uniqueId)
        })
      this.message = 'Successfully added person'
      setTimeout(() => {
        this.message = null
      }, 5000)
    }
  }
}
</script>

<style scoped>

</style>
