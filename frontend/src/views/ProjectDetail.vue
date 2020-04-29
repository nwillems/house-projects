<template>
<div class="project-detail container">
  <div class="row">
    <div class="col-sm-12">
      <project-form v-model="project"></project-form>

      <button class="primary " v-on:click="makeNewProposal">Add proposal</button>
    </div>
  </div>
  <div class="row" v-if="incommingProposals.length"><div class="col-sm-12">
    <table  class="striped hoverable horizontal">
      <thead>
        <tr>
          <th>Contractor</th>
          <th>Offer</th>
          <th>State</th>
          <th>Response</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="proposal in incommingProposals" :key="proposal.id" v-bind:class="{ 'primary': proposal.is_within_budget }">
          <!--  -->
          <td data-label="Contractor">{{ proposal.contractor}} </td>
          <td data-label="Offer">{{ proposal.offer }} </td>
          <td data-label="State">{{ proposal.state }} </td>
          <td data-label="Response">{{ proposal.contractor_response }} </td>
        </tr>
      </tbody>
    </table>
  </div></div>

  <div class="row"><div class="col-sm-12">
    <table  class="striped hoverable">
      <caption>All proposals</caption>
      <thead>
        <tr>
          <th>Contractor</th>
          <th>Offer</th>
          <th>State</th>
          <th>Response</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="proposal in allProposals" :key="proposal.id">
          <!--  -->
          <td data-label="Contractor">{{ proposal.contractor}}</td>
          <td data-label="Offer">{{ proposal.offer }}</td>
          <td data-label="State">{{ proposal.state }}</td>
          <td data-label="Response">{{ proposal.contractor_response }}</td>
          <td  data-label="Actions">
            <span class="icon-edit" v-on:click="editProposal(proposal)"></span>
          </td>
        </tr>
      </tbody>
    </table>
    This is where all the projects go - possibly just in a table
  </div></div>

  <input type="checkbox" id="proposal-form-modal" class="modal" v-model="showProposalEditForm">
  <div class="row modal-row">
    <div class="col-sm-12 col-md-4 col-md-offset-4">
      <div class="card fluid">
        <div class="section"><h4>New/Edit Proposal</h4> <label for="proposal-form-modal" class="modal-close" ></label></div>
        <div class="section">
          <proposal-form v-model="proposalFormModel" v-on:save="save"></proposal-form>
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<style>

tr.primary > td {
  background: #85bae5; /* var(--table-body-hover-back-color) */
}

</style>

<script>
import { HTTP } from '@/components/CommonHttp.js'
import ProjectForm from '@/components/ProjectForm.vue'
import ProposalForm from '@/components/ProposalForm.vue'

export default {
  name: 'ProjectDetail',
  components: {
    ProjectForm,
    ProposalForm
  },
  data () {
    return {
      project: { proposals: [] },
      showProposalEditForm: false,
      proposalFormModel: {}
    }
  },
  created () {
    this.fetchData()
  },
  methods: {
    fetchData () {
      const projectId = this.$route.params.projectid
      HTTP.get(`api/projects/${projectId}/`).then(response => {
        this.project = response.data
      })
    },
    save (proposal) {
      HTTP.post('api/proposals/', proposal)
        .then(() => {
          this.showProposalEditForm = false
          this.fetchData()
        })
    },
    makeNewProposal () {
      const projectId = this.$route.params.projectid
      this.proposalFormModel = {
        project: `/api/projects/${projectId}/`,
        contractor: '',
        contractor_email: '',
        contractor_response: '',
        offer: 0,
        state: 'OPEN'
      }
      this.showProposalEditForm = true
    },
    editProposal (proposal) {
      this.proposalFormModel = proposal
      this.showProposalEditForm = true
    }
  },
  computed: {
    incommingProposals: function () {
      const ps = this.project.proposals
      return ps.filter(proposal => proposal.state === 'APPROVED' || proposal.state === 'VALIDATING')
    },
    allProposals: function () {
      return this.project.proposals
    }
  }
}
</script>
