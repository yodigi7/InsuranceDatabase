<template>
    <div class="container-fluid">
      <legend class="border-bottom pb-2 pt-4">Phones</legend>
      <div class="card row" v-for="(phone, index) in phones" :key="phone">
        <div class="card-body">
          <Phone v-bind:ref="index" class="col-sm-8"></Phone>
          <button type="button" class="close col-sm-1" v-on:click="deletePhone(phone)" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
      </div>
      <button type="button" class="btn btn-info" v-on:click="addPhone">
        Add phone
      </button>
    </div>
</template>

<script>
import Phone from './Phone'
export default {
  name: 'PhoneList',
  components: {Phone},
  data () {
    return {
      phones: []
    }
  },
  methods: {
    deletePhone (phone) {
      this.phones.splice(this.phones.indexOf(phone), 1)
    },
    addPhone () {
      if (this.phones.length > 0) {
        this.phones.push(this.phones[this.phones.length - 1] + 1)
      } else {
        this.phones.push(1)
      }
    },
    add (uniqueId) {
      for (var index in this.$refs) {
        this.$refs[index][0].add(uniqueId)
      }
    }
  }
}
</script>

<style scoped>

</style>
