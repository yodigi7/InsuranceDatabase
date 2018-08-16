<template>
    <div class="container-fluid">
      <legend class="pb-2 pt-1">Phones</legend>
      <div class="card row" v-for="(phone, index) in phones" :key="phone">
        <div class="card-body p-1">
          <div class="row px-1">
            <Phone v-bind:ref="index" class="col-sm-11"></Phone>
            <button type="button" class="close col-1" v-on:click="deletePhone(phone)" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
        </div>
      </div>
      <button type="button" class="btn btn-info mt-2" v-on:click="addPhone">
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
      this.$nextTick(() => {
        this.$refs[this.phones.length - 1][0].setFocus()
      })
    },
    add (uniqueId) {
      for (let index in this.$refs) {
        this.$refs[index][0].add(uniqueId)
      }
    },
    reset () {
      this.phones = []
    }
  }
}
</script>

<style scoped>
Phone {
  margin-right: -100px;
}
</style>
