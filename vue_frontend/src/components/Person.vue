<template>
  <div>
    <div class="row">
      <div class="form-group col-sm-1 pr-0">
        <label class="form-control-label" for="prefix">Prefix</label>
        <select class="form-control" id="prefix" v-model="prefix">
          <option>Mrs.</option>
          <option>Ms.</option>
          <option>Mr.</option>
          <option>Dr.</option>
        </select>
      </div>
      <div class="form-group col-sm-3 ml-0">
        <label class="form-control-label" for="first_name">First Name</label>
        <input class="form-control" id="first_name" type="text" v-model="firstName"/>
      </div>
      <div class="form-group col-sm-3">
        <label class="form-control-label" for="middle_name">Middle Name</label>
        <input class="form-control" id="middle_name" type="text" v-model="middleName"/>
      </div>
      <div class="form-group col-sm-4">
        <label class="form-control-label" for="last_name">Last Name</label>
        <input class="form-control" id="last_name" type="text" v-model="lastName"/>
      </div>
      <div class="form-group col-sm-1 pl-0">
        <label class="form-control-label" for="suffix">Suffix</label>
        <select class="form-control" id="suffix" v-model="suffix">
          <option>Sr.</option>
          <option>Jr.</option>
          <option>I</option>
          <option>II</option>
          <option>III</option>
          <option>IV</option>
          <option>PhD</option>
        </select>
      </div>
    </div>
    <div class="form-group">
      <label class="form-control-label" for="address">Address</label>
      <input class="form-control" id="address" type="text" v-model="address"/>
    </div>
    <div class="form-group">
      <label class="form-control-label" for="mailing_address">Mailing Address</label>
      <small>(if different)</small>
      <input class="form-control" id="mailing_address" type="text" v-model="mailingAddress"/>
    </div>
    <div class="row">
      <div class="form-group col-10">
        <label class="form-control-label" for="birth_date">Birth Date</label>
        <input class="form-control" id="birth_date" type="date" v-model="birthDate"/>
      </div>
      <div class="form-group col-sm-2">
        <label class="form-control-label" for="customer_type">Customer Type</label>
        <select class="form-control" id="customer_type" v-model="customerType">
          <option>Active</option>
          <option>Inactive</option>
          <option>Prospect</option>
        </select>
      </div>
    </div>
    <div class="form-group">
      <label class="form-control-label" for="social_security_number">Social Security Number</label>
      <input class="form-control" id="social_security_number" type="number" v-model="socialSecurityNumber"/>
    </div>
    <div class="row">
      <div class="form-group col-5">
        <label class="form-control-label" for="height">Height</label>
        <input class="form-control" id="height" type="text" v-model="height"/>
      </div>
      <div class="form-group col-5">
        <label class="form-control-label" for="weight">Weight</label>
        <input class="form-control" id="weight" type="number" v-model="weight"/>
      </div>
      <div class="form-group col-2">
        <label class="form-control-label" for="can_use_credit_score">Can Use Credit Score</label>
        <input class="form-control" id="can_use_credit_score" type="checkbox" v-model="canUseCreditScore"/>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Person',
  props: ['unique_id'],
  data () {
    return {
      uniqueId: '',
      prefix: '',
      firstName: '',
      middleName: '',
      lastName: '',
      suffix: '',
      address: '',
      mailingAddress: '',
      birthDate: '',
      customerType: '',
      height: '',
      weight: '',
      socialSecurityNumber: '',
      canUseCreditScore: ''
    }
  },
  methods: {
    add () {
      fetch('localhost:5000/api/person', {
        body: JSON.stringify(this.$data),
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        }
      })
    }
  }
}
</script>

<style scoped>

</style>
