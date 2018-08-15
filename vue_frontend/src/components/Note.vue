<template>
  <div class="container-fluid">
    <label class="form-control-label" for="note">Note</label>
    <textarea class="form-control" id="note" v-model="note"></textarea>
  </div>
</template>

<script>
export default {
  name: 'Notes',
  data () {
    return {
      note: ''
    }
  },
  methods: {
    add (personId) {
      if (this.note) {
        console.log('adding person note')
        fetch('http://localhost:5000/api/person-notes', {
          method: 'POST',
          body: JSON.stringify({
            personId: personId,
            note: this.$data.note
          }),
          headers: {
            'Content-Type': 'application/json'
          }
        }).then(() => {
          this.$data.note = ''
        })
      }
    }
  }
}
</script>

<style scoped>

</style>
