<template>
  <div class="container">
    <FlashMessage v-bind:message="message" type="success"></FlashMessage>
    <form method="POST" @submit.prevent="modifyPerson">
      <fieldset class="form-group">
        <legend class="border-bottom mb-4">Modify a Person</legend>
        <div class="row">
          <Person ref="person"></Person>
          <Note ref="note"></Note>
          <PhoneList ref="phoneList"></PhoneList>
        </div>
      </fieldset>
      <div class="form-group float-left">
        <button class="btn btn-info">Save</button>
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
  name: 'ModifyPerson',
  components: {Person, FlashMessage, PhoneList, Note},
  data () {
    return {
      message: null
    }
  },
  mounted: function () {
    let id = this.$route.params.id
    this.$refs.person.load(id)
    this.$refs.note.load(id)
    this.$refs.phoneList.load(id)
    this.$refs.person.setFocus()
  },
  methods: {
    modifyPerson () {
      this.$refs.person.update(this.$route.params.id)
      this.$refs.note.update(this.$route.params.id)
      this.$refs.phoneList.update(this.$route.params.id)
      this.message = 'Successfully Updated'
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
