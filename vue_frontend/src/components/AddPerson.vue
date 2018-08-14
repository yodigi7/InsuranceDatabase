<template>
  <div class="container">
    <form method="POST" action="" @submit.prevent="addPerson">
      <fieldset class="form-group">
        <legend class="border-bottom mb-4">Add a Person</legend>
        <div class="row">
          <Person ref="person"></Person>
        </div>
      </fieldset>
      <div class="form-group">
        <button class="btn btn-info">Submit</button>
      </div>
    </form>
  </div>
</template>

<script>
import Person from './Person'
export default {
  name: 'AddPerson',
  components: {Person},
  methods: {
    addPerson () {
      this.$refs.person.add()
    }
  }
}
</script>

<style scoped>

</style>
