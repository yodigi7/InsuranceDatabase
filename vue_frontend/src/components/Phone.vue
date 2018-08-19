<template>
  <div class="container row">
    <div class="form-group col-sm-8 mb-0">
      <label class="form-control-label" for="phone-number">Phone</label>
      <input class="form-control form-control-sm mb-1" type="number" id="phone-number" v-model="phoneNumber" ref="phoneNumber"/>
    </div>
    <div class="form-group col-sm-4 mb-0">
      <label class="form-control-label" for="type">Type</label>
      <select class="form-control form-control-sm" id="type" v-model="type">
        <option></option>
        <option>Cell</option>
        <option>Other</option>
        <option>Home</option>
        <option>Work</option>
      </select>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Phone',
  props: ['phoneId'],
  data () {
    return {
      phoneNumber: null,
      type: null
    }
  },
  mounted: function () {
    console.log(this.phoneId)
    if (this.phoneId) {
      fetch('http://localhost:5000/api/phone/' + this.phoneId)
        .then(response => response.json())
        .then((response) => {
          console.log(response)
          console.log()
          this.phoneNumber = response.phone_number
          this.type = response.type
        })
    }
  },
  methods: {
    add (personId) {
      console.log(personId)
      fetch('http://localhost:5000/api/phone', {
        body: JSON.stringify({
          personId: personId,
          phoneNumber: this.phoneNumber,
          type: this.type
        }),
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        }
      })
        .then(() => {
          this.phoneNumber = null
          this.type = null
        })
    },
    setFocus () {
      this.$refs.phoneNumber.focus()
    }
  }
}
</script>

<style scoped>

</style>
