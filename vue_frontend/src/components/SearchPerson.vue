<template>
  <div class="container">
    <form @submit.prevent="searchPerson">
      <fieldset class="form-group">
        <legend class="border-bottom mb-4">Search for People</legend>
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
export default {
  name: 'SearchPerson',
  components: {Person},
  data () {
    return {
      ids: []
    }
  },
  methods: {
    searchPerson () {
      console.log(this.$refs.person.$data)
      fetch('http://localhost:5000/api/search-person', {
        method: 'POST',
        body: JSON.stringify(this.$refs.person.$data),
        headers: {
          'Content-Type': 'application/json'
        }
      }).then(response => response.json())
        .then((response) => {
          this.ids = response.ids
        })
        .then(() => {
          this.$router.push({ name: 'ListOfPeople', params: {ids: this.ids.join(',')} })
        })
    }
  }
}
</script>

<style scoped>

</style>
