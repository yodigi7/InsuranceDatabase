<template>
  <div class="container">
    <FlashMessage v-bind:message="message" type="success"></FlashMessage>
    <form method="POST" @submit.prevent="modifyPerson">
      <fieldset class="form-group">
        <legend class="border-bottom mb-4">Modify a Person</legend>
        <div class="row">
          <Person ref="person"></Person>
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
export default {
  name: 'ModifyPerson',
  components: {Person, FlashMessage},
  data () {
    return {
      message: null
    }
  },
  mounted: function () {
    this.$refs.person.load(this.$route.params.id)
  },
  methods: {
    modifyPerson () {
      this.$refs.person.update(this.$route.params.id)
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
