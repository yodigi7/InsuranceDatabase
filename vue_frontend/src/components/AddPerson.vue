<template>
  <div class="container-fluid col-10">
    <FlashMessage v-bind:message="message" type="success"></FlashMessage>
    <form v-on:submit.prevent="addPersonAndNote">
      <fieldset class="form-group">
        <legend class="border-bottom pb-2">Add a Person</legend>
        <Person ref="person"></Person>
        <Note ref="note"></Note>
        <PhoneList ref="phoneList"></PhoneList>
      </fieldset>
      <div class="form-group float-right">
        <button class="btn btn-info">Submit</button>
      </div>
    </form>
  </div>
</template>

<script>
import Person from './Person'
import FlashMessage from './FlashMessage'
import Note from './Note'
import PhoneList from './PhoneList'
export default {
  name: 'AddPerson',
  components: {PhoneList, Person, FlashMessage, Note},
  data () {
    return {
      message: null
    }
  },
  methods: {
    addPersonAndNote () {
      this.$refs.person.add()
        .then((uniqueId) => {
          console.log(this.$refs)
          this.$refs.note.add(uniqueId)
          this.$refs.phoneList.add(uniqueId)
        })
        .then(() => {
          this.$refs.note.reset()
          this.$refs.phoneList.reset()
        })
      this.message = 'Successfully added person'
      setTimeout(() => {
        this.message = null
      }, 5000)
    }
  },
  mounted () {
    console.log(this.$refs.person)
    this.$refs.person.setFocus()
  }
}
</script>

<style scoped>
#note {
  padding-left: 4px;
  padding-right: 4px;
}
</style>
