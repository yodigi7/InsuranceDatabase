<template>
  <div v-if="people">
    <div v-for="person in this.people" v-bind:key="person.unique_id">
      <CollapsiblePerson v-bind:person="person"></CollapsiblePerson>
    </div>
  </div>
</template>

<script>
import CollapsiblePerson from './CollapsiblePerson'
export default {
  name: 'ListOfPeople',
  components: { CollapsiblePerson },
  props: ['ids'],
  data () {
    return {
      people: []
    }
  },
  mounted: function () {
    console.log('here')
    console.log(this.ids)
    for (let i = 0; i < this.$props.ids.length; i++) {
      fetch('http://localhost:5000/api/person/' + this.$props.ids[i])
        .then(response => response.json())
        .then(response => {
          console.log(response)
          this.people.push(response)
        })
        .then(() => {
          console.log('people data')
          console.log(this.people.length)
        })
    }
  }
}
</script>

<style scoped>

</style>
