<!--suppress ALL -->
<template>
    <div class="container-fluid">
      <legend class="pb-2 pt-1">Phones</legend>
      <div v-if="phoneIds" class="card row" v-for="(phoneId, index) in phoneIds">
        <div class="card-body p-1">
          <div class="row px-1">
            <Phone v-bind:ref="'phoneId' + phoneId" v-bind:unique_id="phoneId" v-bind:phoneId="phoneId" class="col-sm-11"></Phone>
            <button type="button" class="close col-1" v-on:click="deletePhoneById(phoneId)" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
        </div>
      </div>
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
      phones: [],
      phoneIds: []
    }
  },
  methods: {
    deletePhone (phone) {
      this.phones.splice(this.phones.indexOf(phone), 1)
    },
    deletePhoneById (phoneId) {
      fetch('http://localhost:5000/api/phone/' + phoneId, {
        method: 'DELETE'
      })
      this.phones.splice(this.phoneIds.indexOf(phoneId), 1)
    },
    addPhone () {
      if (this.phones.length > 0) {
        this.phones.push(this.phones[this.phones.length - 1] + 1)
      } else {
        this.phones.push(1)
      }
      console.log(this.$refs)
      this.$nextTick(() => {
        this.$refs[this.phones.length - 1][0].setFocus()
      })
    },
    add (uniqueId) {
      console.log(this.$refs)
      for (let index in this.$refs) {
        this.$refs[index][0].add(uniqueId)
      }
    },
    load (personId) {
      console.log(personId)
      fetch('http://localhost:5000/api/phones-by-person/' + personId)
        .then(response => response.json())
        .then((response) => {
          console.log(response.phones)
          this.phoneIds = response.phones.map(x => x.unique_id)
          console.log(this.phoneIds)
        })
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
