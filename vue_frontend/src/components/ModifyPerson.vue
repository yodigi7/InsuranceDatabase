<template>
  <div class="container">
    <form method="POST" @submit.prevent="modifyPerson">
      <fieldset class="form-group">
        <legend class="border-bottom mb-4">Modify a Person</legend>
        <div class="row">
          <Person ref="person"></Person>
        </div>
      </fieldset>
      <div class="form-group float-left">
        <button class="btn btn-info">Modify</button>
      </div>
    </form>
  </div>
</template>

<script>
import Person from './Person'
export default {
  name: 'ModifyPerson',
  components: {Person},
  mounted: function () {
    this.$refs.person.load(this.$route.params.id)
  },
  methods: {
    modifyPerson () {
      this.$refs.person.update()
    }
  }
}
</script>

<style scoped>

</style>
