<template>
  <div>
    <div v-for="person in people" v-bind:key="person.unique_id">
      <CollapsiblePerson v-bind:person="person"></CollapsiblePerson>
    </div>
  </div>
</template>

<script>
import CollapsiblePerson from './CollapsiblePerson'
export default {
  name: 'ListPeople',
  components: { CollapsiblePerson },
  data () {
    return {
      people: []
    }
  },
  mounted: function () {
    console.log(this.$route.params)
    fetch('http://localhost:5000/api/person', {
      headers: {
        page: this.$route.params.page
      }
    })
      .then(response => response.json())
      .then((data) => {
        console.log(data.people)
        this.people = data.people
      })
  }
}
</script>

<style scoped>

</style>
