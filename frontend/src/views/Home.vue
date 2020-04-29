<template>
  <div class="projectlist container">
  <div class="row"><div class="col-sm-1 col-sm-offset-11">
    <button class="primary" v-on:click="showNewProjectModal = true">Add project</button>
  </div></div>

  <div class="row"><div class="col-sm-12">
    <project-list v-bind:projects="projects"></project-list>
  </div></div>

  <input type="checkbox" id="new-project-modal" class="modal" v-model="showNewProjectModal">
  <div class="row modal-row">
    <div class="col-sm-12 col-md-4 col-md-offset-4">
      <div class="card fluid">
        <div class="section"><h4>New Project</h4> <label for="new-project-modal" class="modal-close" ></label></div>
        <div class="section">
          <project-form v-model="newProject" v-on:save="save"></project-form>
        </div>
      </div>
    </div>
  </div>

  </div>
</template>

<style scoped>
.modal-row > div {
  margin-top: 1rem;
}

#new-project-modal + div .card {
  max-height: 100vh;
}
</style>

<script>
import ProjectList from '@/components/ProjectList.vue'
import ProjectForm from '@/components/ProjectForm.vue'
import { HTTP, paginatedFetcher } from '@/components/CommonHttp.js'

export default {
  name: 'Home',
  components: {
    ProjectList,
    ProjectForm
  },
  data: function () {
    return {
      projects: [],
      newProject: {
        title: '',
        budget: 0,
        deadline: '',
        description: ''
      },
      showNewProjectModal: false
    }
  },
  created () {
    this.fetchData()
  },
  methods: {
    fetchData () {
      paginatedFetcher('api/projects/', (data) => {
        this.projects = this.projects.concat(data.results)
      })
    },
    save (project) {
      HTTP.post('api/projects/', project)
        .then(() => {
          this.showNewProjectModal = false
          this.projects = []
          this.fetchData()
        })
    }
  }
}
</script>
