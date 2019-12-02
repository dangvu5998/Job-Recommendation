<template>
  <div class="site-wrap">

    <div class="site-mobile-menu site-navbar-target">
      <div class="site-mobile-menu-header">
        <div class="site-mobile-menu-close mt-3">
          <span class="icon-close2 js-menu-toggle"></span>
        </div>
      </div>
      <div class="site-mobile-menu-body"></div>
    </div> <!-- .site-mobile-menu -->


    <!-- NAVBAR -->
    <header class="site-navbar mt-3">
      <div class="container-fluid">
        <div class="row align-items-center">
          <div class="site-logo col-6"><a href="/">Careers</a></div>

          <nav class="mx-auto site-navigation">
            <ul class="site-menu js-clone-nav d-none d-xl-block ml-0 pl-0">
              <li><a href="/" class="nav-link">Trang chủ</a></li>
            </ul>
          </nav>
        </div>
      </div>
    </header>

    <!-- HOME -->
    <section class="home-section section-hero inner-page overlay bg-image" style="background-image: url('images/hero_1.jpg');"
      id="home-section">

      <div class="container">
        <div class="row align-items-center justify-content-center" style="padding-top: 0;">
          <div class="col-md-12">
            <div class="mb-5 text-center">
              <h1 class="text-white font-weight-bold">Job Listings</h1>
              <p>Tìm công việc bạn mong muốn</p>
              <br/>
              <div class="form">
                <form method="post" class="search-jobs-form">
              <div class="row mb-5">
                <div class="col-12 col-sm-6 col-md-6 col-lg-6 mb-4 mb-lg-0">
                  <input type="text"
                    class="form-control form-control-lg"
                    placeholder="Tên công việc, keywords..."
                    v-model="description"
                    />
                </div>
                <div class="col-12 col-sm-6 col-md-6 col-lg-2 mb-4 mb-lg-0">
                  <input type="text"
                    class="form-control form-control-lg"
                    placeholder="Nơi làm việc"
                    v-model="address"
                  />
                </div>
                <div class="col-12 col-sm-6 col-md-6 col-lg-2 mb-4 mb-lg-0">
                  <input type="text"
                    class="form-control form-control-lg"
                    placeholder="Mức lương mong muốn"
                    v-model="salary"
                  />
                </div>
                <div class="col-12 col-sm-6 col-md-6 col-lg-2 mb-4 mb-lg-0">
                  <button type="button"
                    class="btn btn-primary btn-lg btn-block text-white btn-search"
                    v-on:click="searchJob()"
                  >
                    <span class="icon-search icon mr-2"></span>
                      Tìm việc
                  </button>
                </div>
              </div>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  <br/><br/>

    <section class="site-section" style="padding: 0">
      <div class="container" style="padding-bottom: 30px;">
        <div class="mb-1">
          <div v-for="job in jobs" v-bind:key="job.id" class="row align-items-start job-item border-bottom pb-3 mb-3 pt-3">
            <div class="col-md-7">
              <h2><a :href="'jobs/' + job.id">{{ job.title }}</a> </h2>
              <p class="meta">Công ty: <strong>{{ job.company_title }}</strong></p>
            </div>
            <div class="col-md-3 text-left">
              <h3>{{ job.address.toUpperCase() }}</h3>
            </div>
            <div class="col-md-2 text-md-right">
              <strong class="text-black">{{ showSalary(job.salary_min) }} &mdash; {{ showSalary(job.salary_max) }}</strong>
            </div>
          </div>

        </div>

        <div class="row pagination-wrap">

          <div class="col-md-6 text-center text-md-left">
            <div class="custom-pagination ml-auto">
              <a v-if="page > 1" v-on:click="changePage(page + 1)" class="prev">Trước</a>
              <div class="d-inline-block">
                <a v-for="i in paginations" :key="i"
                 v-on:click="changePage(i)" :class="{active: i == page}">{{i}}</a>
              </div>
              <a v-on:click="changePage(page + 1)" class="next">Sau</a>
            </div>
          </div>
        </div>

      </div>
    </section>

  </div>
</template>
<script>
import axios from 'axios'
export default {
  data: () => ({
    description: null,
    salary: null,
    address:null,
    page: null,
    jobs: [],
    baseUrl: null,
    paginations: []
  }),
  created() {
    const urlParams = new URLSearchParams(window.location.search);
    this.description = urlParams.get('description');
    this.salary = urlParams.get('salary');
    this.address = urlParams.get('address');
    this.page = parseInt(urlParams.get('page'))
    if (isNaN(this.page)) {
      this.page = 1
    }
    for (let i = -2; i < 3; i++) {
      if (this.page + i > 0)
        this.paginations.push(this.page + i)
    }
    this.baseUrl = `/search?description=${this.description}&address=${this.address}&salary=${this.salary}`
    let limit = 10
    let offset = (this.page - 1) * limit
    axios.get(`/api/search?description=${this.description}&salary=${this.salary}&address=${this.address}
    &limit=${limit}&offset=${offset}`)
    .then(res => {
      console.log(res)
      this.jobs = res.data.jobs
    }).catch(err => {
      console.log(err)
    })

  },
  methods: {
    showSalary(salary) {
      if (salary > 1000000) {
        return String((salary / 1000000).toFixed(2)) + 'tr'
      }
    },
    searchJob() {
      if (!this.description) {
        return
      }
      let redirectUrl = `/search?description=${this.description}`
      if (this.address) {
        redirectUrl = `${redirectUrl}&address=${this.address}`
      }
      if (this.salary) {
        redirectUrl = `${redirectUrl}&salary=${this.salary}`
      }
      window.location = redirectUrl
    },
    changePage(page) {
      window.location = `${this.baseUrl}&page=${page}`
    }
  }
}
</script>