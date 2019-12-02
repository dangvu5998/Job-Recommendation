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
            <a href="#" class="site-menu-toggle js-menu-toggle d-inline-block d-xl-none mt-lg-2 ml-3"><span
                class="icon-menu h3 m-0 p-0 mt-2"></span></a>
          </div>

        </div>
    </header>

    <!-- HOME -->
    <section class="section-hero overlay inner-page bg-image" style="background-image: url('/images/hero_1.jpg');"
      id="home-section">
      <div class="container">
        <div class="row">
          <div class="col-md-7">
            <h1 class="text-white font-weight-bold">{{ title }}</h1>
          </div>
        </div>
      </div>
    </section>
    
    
    <section class="site-section" style="padding: 30px">
      <div class="container">
        <div class="row align-items-center mb-5">
          <div class="col-lg-8 mb-4 mb-lg-0">
            <div class="d-flex align-items-center">
              <div class="border p-2 d-inline-block mr-3 rounded">
                <img src="/images/featured-listing-1.jpg" alt="Free Website Template By Free-Template.co">
              </div>
              <div>
                <h2>{{ title }}</h2>
                <div>
                  <span class="ml-0 mr-2 mb-2"><span class="icon-briefcase mr-2"></span>{{ company_title }}</span>
                  <span class="m-2"><span class="icon-room mr-2"></span>{{ address }}</span>
                  <span class="m-2"><span class="icon-clock-o mr-2"></span><span class="text-primary">Full
                      Time</span></span>
                </div>
              </div>
            </div>
          </div>
          <div class="col-lg-4">
          </div>
        </div>
        <div class="row">
          <div class="col-lg-8">
            <div class="mb-5">
              <h3 class="h5 d-flex align-items-center mb-4 text-primary">
                <span class="icon-align-left mr-3"></span>Mô tả công việc</h3>
                <p v-html="description"></p>
            </div>
            <div class="mb-5" v-if="skills.length > 0">
              <h3 class="h5 d-flex align-items-center mb-4 text-primary"><span
                  class="icon-rocket mr-3"></span>Kỹ năng</h3>
              <ul class="list-unstyled m-0 p-0">
                <li v-for="skill in skills" :key="skill" class="d-flex align-items-start mb-2"><span
                    class="icon-check_circle mr-2 text-muted"></span><span>{{ skill }}</span></li>
              </ul>
            </div>
    
            <div class="mb-5" v-if="level">
              <h3 class="h5 d-flex align-items-center mb-4 text-primary"><span class="icon-book mr-3"></span>Cấp độ</h3>
              <ul class="list-unstyled m-0 p-0">
                <li class="d-flex align-items-start mb-2"><span
                    class="icon-check_circle mr-2 text-muted"></span><span>{{ level }}</span></li>
              </ul>
            </div>
    
            <div class="mb-5" v-if="benefits.length > 0">
              <h3 class="h5 d-flex align-items-center mb-4 text-primary"><span class="icon-turned_in mr-3"></span>Quyền lợi</h3>
              <ul class="list-unstyled m-0 p-0">
                <li v-for="benefit in benefits" :key="benefit" class="d-flex align-items-start mb-2"><span
                    class="icon-check_circle mr-2 text-muted"></span><span>{{ benefit }}</span></li>
              </ul>
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
  data() {
    return {
      address: null,
      company_title: null,
      description: null,
      id: null,
      level: null,
      title: null,
      salary_min: null,
      salary_max: null,
      skills: [],
      benefits: [],
    }
  },
  created() {
    let pathname = location.pathname
    let jobId = pathname.split('/').pop()
    axios.get(`/api/jobs/${jobId}`).then(res => {
      console.log(res)
      this.address = res.data.job.address.toUpperCase()
      this.company_title = res.data.job.company_title
      this.title = res.data.job.title
      this.description = res.data.job.description
      this.level = res.data.job.level
      this.level = this.level.charAt(0).toUpperCase() + this.level.slice(1);
      this.salary_min = res.data.job.salary_min
      this.salary_max = res.data.job.salary_max
      this.skills = res.data.job.skills
      this.benefits = res.data.job.benefits
    }).catch(err => {
      console.log(err)
    })
  }
}
</script>