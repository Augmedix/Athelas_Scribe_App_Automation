import hudson.model.Result
import static groovy.io.FileType.FILES  //isort: skip

properties(
      [
          parameters([
              [$class: 'ChoiceParameter',
                  choiceType: 'PT_SINGLE_SELECT',
                  description: 'Select an ENV to run test.',
                  name: 'ENV',
                  script: [$class: 'GroovyScript',
                      script: [
                          classpath: [],
                          sandbox: true,
                          script: """
                              return['staging': 'STAGING:selected', 'dev': 'DEV', 'prod':'LIVE', 'dr':'DR']
                          """.stripIndent()
                      ]
                  ]
              ],

              [$class: 'CascadeChoiceParameter',
                  choiceType: 'PT_SINGLE_SELECT',
                  description: 'Select a URL.',
                  name: 'TEST_URL',
                  referencedParameters: 'ENV',
                  script: [$class: 'GroovyScript',
                      script: [
                          classpath: [],
                          sandbox: true,
                          script: """
                              if (ENV == 'dev') {
                                  return[
                                          'https://dev-scribe1.augmedix.com':'DEV-1 [https://dev-scribe1.augmedix.com]',
                                          'https://dev-scribe2.augmedix.com':'DEV-2 [https://dev-scribe2.augmedix.com]',
                                          'https://dev-scribe3.augmedix.com':'DEV-3 [https://dev-scribe3.augmedix.com]',
                                          'https://dev-scribe4.augmedix.com':'DEV-4 [https://dev-scribe4.augmedix.com]',
                                          'https://dev-scribe5.augmedix.com':'DEV-5 [https://dev-scribe5.augmedix.com]',
                                          'https://dev-scribe6.augmedix.com':'DEV-6 [https://dev-scribe6.augmedix.com]:selected',
                                          'https://dev-scribe7.augmedix.com':'DEV-7 [https://dev-scribe7.augmedix.com]',
                                          'https://dev-scribe8.augmedix.com':'DEV-8 [https://dev-scribe8.augmedix.com]',
                                          'https://dev-scribe9.augmedix.com':'DEV-9 [https://dev-scribe9.augmedix.com]',
                                          'https://dev-scribe10.augmedix.com':'DEV-10 [https://dev-scribe10.augmedix.com]',
                                          'https://dev-scribe11.augmedix.com':'DEV-11 [https://dev-scribe11.augmedix.com]',
                                          'https://dev-scribe12.augmedix.com':'DEV-12 [https://dev-scribe12.augmedix.com]'
                                      ]
                              }
                              else if(ENV == 'staging'){
                                  return ['https://staging-scribe.augmedix.com:selected': 'STAGING [https://staging-scribe.augmedix.com]']
                              }else if(ENV == 'prod'){
                                  return ['https://scribe.augmedix.com': 'LIVE [https://scribe.augmedix.com]']
                              }else{
                                  return ['https://r2-scribe.augmedix.com': 'DR [https://r2-scribe.augmedix.com]']
                              }
                          """.stripIndent()
                      ]
                  ]
              ],

              choice(name: 'TESTTYPE', choices: ['SANITY', 'REGRESSION', 'REGRESSION_EXT'], description: 'Select any of the testing types. REGRESSION_EXT stands for Extended Regression.'),

              text(name: 'BROWSER_VERSION', defaultValue: '117'),

              choice(name: 'PLATFORM_NAME', choices: ['iOS', 'Android']),
              text(name: 'DEVICE_NAME', defaultValue: 'iPhone 13'),
              text(name: 'DEVICE_OS_VERSION', defaultValue: '13'),
              text(name: 'APK_VERSION', defaultValue: '20221474'),

              [$class: 'CascadeChoiceParameter', choiceType: 'PT_SINGLE_SELECT', description: 'Select the threshold value for SANITY to trigger Regression and Ext Regression.',
              name: 'THRESHOLD',
              referencedParameters: 'TESTTYPE',
              script: [$class: 'GroovyScript',
              script: [
              classpath: [],
              sandbox: true,
              script: """
                if (TESTTYPE == 'SANITY') {
                  return [
                  '95': '95',
                  '80': '80',
                  '85': '85',
                  '90': '90'                  ]
                } else {
                  return [
                  '0': 'Not Applicable for Regression and EXT_Regression'
                  ]
                }
                """.stripIndent()
                ]
              ]
          ],

          [$class: 'CascadeChoiceParameter', choiceType: 'PT_SINGLE_SELECT', description: 'Select if you want to run regression test after the sanity test.',
              name: 'RUN_REGRESSION_AFTER_SANITY',
              referencedParameters: 'TESTTYPE',
              script: [$class: 'GroovyScript',
              script: [
              classpath: [],
              sandbox: true,
              script: """
                if (TESTTYPE == 'SANITY') {
                        return [
                            'false': 'No',
                            'true': 'Yes'

                        ]
                    } else {
                        return [
                            'false': 'Not Applicable for Regression and EXT_Regression'
                        ]
                    }
                """.stripIndent()
                ]
              ]
          ],


              [$class: 'CascadeChoiceParameter',
                choiceType: 'PT_CHECKBOX',
                description: 'There are some test cases which are marked as skipped for some reason. Select this option to execute skipped test cases.',
                name: 'EXECUTE_SKIPPED_TCS',
                referencedParameters: 'EXECUTE_FAILED_TCS',
                script: [$class: 'GroovyScript',
                script: [
                    classpath: [],
                    sandbox: true,
                    script: """
                        if(EXECUTE_FAILED_TCS){
                          return[
                               'yes': 'Execute Skipped TC(s):disabled'
                          ]
                        }else{
                          return[
                               'yes': 'Execute Skipped TC(s)'
                          ]
                        }
                        """.stripIndent()
                    ]
                ]
              ],

              booleanParam(name: 'EXECUTE_FAILED_TCS', defaultValue: false, description: 'Whether to execute the latest failed test cases/suites.'),

              [$class: 'CascadeChoiceParameter',
                choiceType: 'PT_CHECKBOX',
                description: 'Check this option if you want to execute all the test suites at one go.',
                name: 'SELECT_ALL',
                referencedParameters: 'EXECUTE_FAILED_TCS',
                script: [$class: 'GroovyScript',
                script: [
                    classpath: [],
                    sandbox: true,
                    script: """
                        if(EXECUTE_FAILED_TCS){
                          return[
                               'select_all': 'Select All:disabled'
                          ]
                        }else{
                          return[
                               'select_all': 'Select All'
                          ]
                        }
                        """.stripIndent()
                  ]
                ]
              ],


              [$class: 'CascadeChoiceParameter',
                choiceType: 'PT_CHECKBOX',
                description: 'List of all test suites. Select test suite(s) you need to execute.',
                name: 'TESTCASE',
                referencedParameters: 'SELECT_ALL, EXECUTE_FAILED_TCS',
                script: [$class: 'GroovyScript',
                fallbackScript: [
                    classpath: [],
                    sandbox: true,
                    script: 'return ["ERROR"]'
                ],
                script: [
                    classpath: [],
                    sandbox: true,
                    script: """
                        if(EXECUTE_FAILED_TCS){
                            return[
                               ${getDisabledTestsuiteList()}
                            ]
                        }
                        if(SELECT_ALL == 'select_all'){
                            return[
                               ${getSelectedTestsuiteList()}
                          ]
                        }else{
                            return[
                               ${getDeSelectedTestsuiteList()}
                          ]
                        }
                        """.stripIndent()
                ]
            ]
        ],
        booleanParam(name: 'STOP_GRID', description: 'Whether to stop the GRID machine after executing test.'),
        hidden(name: 'DEPLOYED_BY', defaultValue: '', description: 'Application Deployed By the user.'),
        hidden(name: 'DEPLOYED_BRANCH', defaultValue: '', description: 'Application Deployed at the branch.')
       ])
      ]
  )

  node {
      cleanWs()
      def repoInformation = checkout scm
      def GIT_COMMIT_HASH = repoInformation.GIT_COMMIT

      wrap([$class: 'BuildUser']) {
         jobUserId = "${BUILD_USER_ID}"
         jobUserName = "${BUILD_USER}"
      }

      currentBuild.displayName = "# ${currentBuild.number} run by ${jobUserId.toUpperCase()} on ${repoInformation.GIT_BRANCH.replace('origin/', '').toUpperCase()}"

      def _gchat_webhook_link = null
      def props = readProperties  file: 'test/ui/resources/jenkins.properties'

      def providedENV = params.ENV
      def providedTestType = params.TESTTYPE
      def providedURL = params.TEST_URL

      try{
         if (jobUserId == 'timer' || jobUserId == 'remoteRequest'){
            _gchat_webhook_link = props["gchat_ci_cd_webhook_link"]
          }else{
            def dev_user_group = props["dev_user_group"]
            def staging_user_group = props["staging_user_group"]
            def live_user_group = props["live_user_group"]

            dev_users_list = dev_user_group.split(',')
            staging_users_list = staging_user_group.split(',')
            live_users_list = live_user_group.split(',')

            if(JOB_NAME == 'GOUIAutomation_RnD'){
               _gchat_webhook_link = props['gchat_rnd_webhook_link']
            }else if(dev_users_list.contains(jobUserId)){
              _gchat_webhook_link = props['gchat_dev_webhook_link']
            }else if(staging_users_list.contains(jobUserId)){
              _gchat_webhook_link = props['gchat_staging_webhook_link']
            }else if(live_users_list.contains(jobUserId)){
              _gchat_webhook_link = props['gchat_webhook_link']
            }else{
                _gchat_webhook_link = props['gchat_webhook_link']
            }
          }

      stage('G-chat Notfication [Starting Test]'){
          def startMessage = "*GOUIAutomation* script execution is started with the following details.\nPlease keep an eye for its completion.\n-----------------------------------------------------------------------------------------------------*\n\n"
          def buildNumber = "*Build number:* " + currentBuild.number + "\n"
          def buildInitiatedBy = "*Build Initiated by:* ${jobUserId.toUpperCase()}\n\n"
          def gitBranch = "*GIT Branch:* ${repoInformation.GIT_BRANCH}\n\n"
          def testType = "*Test type:* ${providedTestType.toUpperCase()}\n"
          def testENV = "*Test ENV:* ${providedENV.toUpperCase()}\n"
          def testURL = "*Test URL:* ${providedURL}\n"
          def buildURL = "*Build URL:* ${JOB_URL}\n\n"
          def deployeApplicationBy = "*SCP Deployed By:* " + env.DEPLOYED_BY.toUpperCase() + "\n"
          def deployeApplicationAt = "*SCP Deployed At:* " + env.DEPLOYED_BRANCH.toUpperCase() + "\n"

          def message = startMessage + buildNumber + buildInitiatedBy + gitBranch + testType + testENV + testURL + buildURL
          if(env.DEPLOYED_BY && env.DEPLOYED_BRANCH){
            message += deployeApplicationBy + deployeApplicationAt
          }
          googlechatnotification message: message, url: _gchat_webhook_link
      }

//       stage('Start Selenium Grid'){
//             sh """
//                 set +x
//                 . ~/.axgo_profile
//                 python3 -m pytest testcases/test_selenium_grid_start_stop.py::TestSeleniumGridStartStop::test_start_selenium_grid -ss -vv --browser-version=${params.BROWSER_VERSION} --alluredir=${WORKSPACE}/allure-results -rA
//                 scp -i ~/.ssh/id_rsa ${WORKSPACE}/resources/docker-compose.yml ubuntu@34.195.102.167:/home/ubuntu/docker-compose.yml
//                 ssh -i ~/.ssh/id_rsa ubuntu@34.195.102.167 sudo docker compose down > /dev/null 2>&1
//                 ssh -i ~/.ssh/id_rsa ubuntu@34.195.102.167 sudo docker compose up -d --scale chrome=50 > /dev/null 2>&1
//                 python3 -m pytest testcases/test_selenium_grid_start_stop.py::TestSeleniumGridStartStop::test_selenium_grid_is_accessible -ss -vv --alluredir=${WORKSPACE}/allure-results -rA
//                 set +x
//             """
//         }

        def parallelTestConfiguration = [
            getParallelConfigurationData()
        ]

        def stepList = prepareBuildStages(parallelTestConfiguration)

        for (def groupOfSteps in stepList) {
          parallel groupOfSteps
        }

        currentBuild.result = "SUCCESS"
      } catch(error) {
        currentBuild.result = "FAILURE"
        echo "The following error occurred: ${error}"
        throw error
      } finally {

        allure([
          includeProperties: false,
          jdk: '',
          properties: [],
          results: [[path: 'target/allure-results']]
        ])

        def gchat_webhook_link = props['gchat_webhook_link']
        String downstream_job_name = props['downstream_job_name']

        def summary = junit testResults: 'testResults/**/*.xml'
        int totalFailed = summary.failCount
        int totalSkipped = summary.skipCount
        int totalCount = summary.totalCount
        int totalExecuted = totalCount - totalSkipped
        double percentFailed = 0

        double percentPassed = 100 - (totalFailed * 100 / totalExecuted)
        int sanity_benchmark = Integer.parseInt(params.THRESHOLD ?: '95')

        if(percentPassed >= sanity_benchmark){
            currentBuild.rawBuild.@result = hudson.model.Result.SUCCESS
        }

        if(((jobUserId == 'remoteRequest' || jobUserId == 'timer') && percentPassed < sanity_benchmark)  || params.STOP_GRID)
        stage('Stop Selenium Grid'){
            sh """
                set +x
                . ~/.bash_profile
                export PYTHONHTTPSVERIFY=0
                python3 -m pytest testcases/test_selenium_grid_start_stop.py::TestSeleniumGridStartStop::test_stop_selenium_grid -ss -vv --alluredir=${WORKSPACE}/allure-results -rA
                set +x
            """
        }

        if(jobUserId == "timer"){
          jobUserId = "SCHEDULER"
        }

        def dev_user_list
        def staging_user_list
        def live_user_list

        stage("G-chat notifier"){
          def now = new Date()

          def summaryMsg = ""

          if(totalCount == 0){
            summaryMsg = "*Ooops!!!* there were no test cases to run. Possibly the user: *${jobUserId}* hasn't selected any of the test suites!\n\n"
          }else{
              percentFailed = totalFailed * 100 / totalExecuted
              if(totalFailed){
                summaryMsg = "${totalFailed} (${percentFailed.round(2)}%) failed out of ${totalExecuted} test cases.\n\n"
              }else{
                summaryMsg = "All passed (out of ${totalExecuted})!!!\n\n"
              }
          }

          def failedTestPropertiesFileInJenkins = "${JENKINS_HOME}/scp_failed_test_${params.TESTTYPE}.properties"
          def failedTestPropertiesFileInResourceFolder = "resources/scp_failed_test_${params.TESTTYPE}.properties"

          if(params.EXECUTE_FAILED_TCS){
              def failedTestProperties = readProperties  file: failedTestPropertiesFileInJenkins
              providedENV = failedTestProperties['env']
              providedURL = failedTestProperties['url']
              providedTestType = failedTestProperties['testtype']
          }

          def startMessage = "*GOUIAutomation script execution is completed. Please see the details (All calculations are EXCLUSIVE of Skipped TCs.):*\n*------------------------------------------------------------------------------------------------------------------------------------------*\n\n"
          def buildStatus = "*Build status:* " + currentBuild.result + "\n"
          def buildNumber = "*Build number:* " + currentBuild.number + "\n"
          def deployeApplicationBy = "*Application Deployed By:* " + env.DEPLOYED_BY.toUpperCase() + "\n"
          def deployeApplicationAt = "*Application Deployed from Branch:* " + env.DEPLOYED_BRANCH.toUpperCase() + "\n"
          def buildInitiatedBy = "*Build Initiated by:* ${jobUserId.toUpperCase()}\n"
          def upstreamProjectName = "*Upstream Project Name:* " + env.UPSTREAM_PROJECT_NAME + "\n"
          def upstreamProjectBuildNo = "*Upstream Project Build number:* " + env.UPSTREAM_PROJECT_BUILD_NO + "\n"
          def buildStarted = "*Build started:* " + env.BUILD_TIMESTAMP + "\n"
          def buildEnded = "*Build ended:* " + now.format("YYYY-MM-dd HH:mm:ss", TimeZone.getTimeZone('BST')) + " BDT\n"
          def buildDuration = "*Duration:* " + currentBuild.durationString + "\n\n"
          def gitBranch = "*GIT Branch:* ${repoInformation.GIT_BRANCH}\n\n"
          def testType = "*Test type:* ${providedTestType.toUpperCase()}\n"
          def testENV = "*Test ENV:* ${providedENV.toUpperCase()}\n"
          def testURL = "*Test URL:* ${providedURL}\n"
          def buildURL = "*Build URL:* ${JOB_URL}\n"
          def reportLink = "*Report URL:* ${BUILD_URL}allure/\n\n"

          def message = ''
          if(env.UPSTREAM_PROJECT_BUILD_NO){
            message = startMessage + summaryMsg + buildStatus + buildNumber + buildInitiatedBy + upstreamProjectName + upstreamProjectBuildNo + buildStarted + buildEnded + buildDuration + gitBranch + testType + testENV + testURL + buildURL + reportLink
          }else{
            message = startMessage + summaryMsg + buildStatus + buildNumber + buildInitiatedBy + buildStarted + buildEnded + buildDuration + gitBranch + testType + testENV + testURL + buildURL + reportLink
          }

          if(env.DEPLOYED_BY && env.DEPLOYED_BRANCH){
            message = startMessage + summaryMsg + buildStatus + buildNumber + buildInitiatedBy + deployeApplicationBy + deployeApplicationAt + buildStarted + buildEnded + buildDuration + gitBranch + testType + testENV + testURL + buildURL + reportLink
          }

          googlechatnotification message: message, url: _gchat_webhook_link
        }

        if(params.TESTTYPE == "SANITY" && (jobUserId == "SCHEDULER" || jobUserId == "remoteRequest")){
            stage('Code Quality Checking'){
                sh """
                    set +x
                    python3 -m pylint -j 0 \$(git ls-files '*.py') --exit-zero --output-format=parseable | tee pylint.json || true
                    set +x
                """
                def pylint = scanForIssues healthy: 95, minimumSeverity: 'HIGH', qualityGates: [[threshold: 0, type: 'TOTAL', unstable: false]], tool: pyLint(pattern: 'pylint.json')
                publishIssues issues: [pylint]

                publishIssues id: 'analysis', name: 'All Issues',
                    issues: [pylint]
            }
        }


        if((percentPassed >= sanity_benchmark && params.TESTTYPE == "SANITY"  &&  (jobUserId == "SCHEDULER" || jobUserId == "remoteRequest")) || (params.RUN_REGRESSION_AFTER_SANITY == true && params.SELECT_ALL == 'select_all')){
          stage("Regression Triggering"){
              print("Sanity successfully done. Triggering core regression...")
              build job: "${downstream_job_name}", parameters: [
                  string(name: "ENV", value: "${params.ENV}"),
                  string(name: "TEST_URL", value: "${params.TEST_URL}"),
                  string(name: "TESTTYPE", value: "REGRESSION"),
                  booleanParam(name: "EXECUTE_FAILED_TCS", value: false),
                  string(name: "THRESHOLD", value: "95"),
                  string(name: "USER", value: "${jobUserId}"),
                  string(name: "UPSTREAM_PROJECT_NAME", value: "${JOB_BASE_NAME}"),
                  string(name: "UPSTREAM_PROJECT_BUILD_NO", value: "${currentBuild.number}")
                ], propagate: false

              stage("Extensive Regression Triggering"){
              print("Sanity and Core Regression successfully done. Triggering extensive regression...")
              build job: "${downstream_job_name}", parameters: [
                  string(name: "ENV", value: "${params.ENV}"),
                  string(name: "TEST_URL", value: "${params.TEST_URL}"),
                  string(name: "TESTTYPE", value: "REGRESSION_EXT"),
                  booleanParam(name: "EXECUTE_FAILED_TCS", value: false),
                  string(name: "THRESHOLD", value: "95"),
                  string(name: "USER", value: "${jobUserId}"),
                  string(name: "UPSTREAM_PROJECT_NAME", value: "${JOB_BASE_NAME}"),
                  string(name: "UPSTREAM_PROJECT_BUILD_NO", value: "${currentBuild.number}")
                ], propagate: false
          }
          }
        }
      }
  }

  @NonCPS
  def getTestsuitePropertiesLoaded(){
    def currentDir = new File("${JENKINS_HOME}/workspace")
    def properties = new Properties()

    files_lst = []
    currentDir.traverse { File file ->
        if (file.name == 'testsuites.properties' && file.absolutePath.contains(JOB_NAME)) {
                def propertiesFile = new File(file.absolutePath)
                propertiesFile.withInputStream{
                    properties.load(it)
                }
        }
    }


    return properties.sort { it.value.toString().toLowerCase()}
  }

  def getFormattedTestsuiteName(String suiteName){
    def testType = ['Sanity', 'Core Regression', 'Extensive Regression']

    def splitted_testsuite_name = suiteName.split(':')
    int index = 0
    testsuite_name_decorated = splitted_testsuite_name[0] + " (" + splitted_testsuite_name.tail().collect({testType[index++] + ": " + it + " min(s)" }).join(' |§| ') + " )"
    return testsuite_name_decorated
  }

  def getEnabledTestsuiteList(){
    def properties = getTestsuitePropertiesLoaded()
    def suite_lst = []
    properties.each {
        def testsuite_name_decorated = getFormattedTestsuiteName(it.value)
        suite_lst.add("'${it.key}': '${testsuite_name_decorated}'")
    }
    return suite_lst
  }

  def getDisabledTestsuiteList(){
    def properties = getTestsuitePropertiesLoaded()
    def suite_lst = []
    properties.each {
        def testsuite_name_decorated = getFormattedTestsuiteName(it.value)
        suite_lst.add("'${it.key}': '${testsuite_name_decorated}:disabled'")
    }
    return suite_lst.join(',')
  }

  def getSelectedTestsuiteList(){
    def properties = getTestsuitePropertiesLoaded()
    def suite_lst = []
    properties.each {
        def testsuite_name_decorated = getFormattedTestsuiteName(it.value)
        suite_lst.add("'${it.key}': '${testsuite_name_decorated}:selected'")
    }
    return suite_lst.join(',')
  }

  def getDeSelectedTestsuiteList(){
    def properties = getTestsuitePropertiesLoaded()
    def suite_lst = []
    properties.each {
        def testsuite_name_decorated = getFormattedTestsuiteName(it.value)
        suite_lst.add("'${it.key}': '${testsuite_name_decorated}'")
    }
    return suite_lst.join(',')
  }

  def getPytestCollectedItems(String fileName){
      def pytest_collected_items = sh (
        script: "set +x;. ~/.bash_profile;python3 -m pytest -m ${params.TESTTYPE.toLowerCase()} ${fileName} --collect-only | grep -Eo 'collected [0-9]+ items?|[0-9]+ deselected|[0-9]+ selected'; set -x",
        returnStdout: true
       ).trim()

       return pytest_collected_items
  }

  def getParallelConfigurationData(){
    def properties = getTestsuitePropertiesLoaded()

    def testsuite_map = [:]
    properties.each {
        testsuite_map.put(it.value.split(":")[0], it.key)
    }

    return testsuite_map
  }


  def prepareBuildStages(List<Map<String,String>> parallelTestConfiguration) {
    def stepList = []

    println('Preparing builds...')

    for (def parallelConfig in  parallelTestConfiguration) {
      def parallelSteps = prepareParallelSteps(parallelConfig)
      stepList.add(parallelSteps)
    }

    println('Finished preparing builds!')

    return stepList
  }


  def prepareParallelSteps(Map<String, String> parallelStepsConfig) {
    def testcases = params.TESTCASE
    String [] testcaseList = testcase.split(',')
    def parallelSteps = [:]

    wrap([$class: 'BuildUser']) {
        jobUserId = "${BUILD_USER_ID}"
    }

  if(jobUserId == "remoteRequest" || jobUserId == "SCHEDULER"){
      parallelStepsConfig.each{
        def key = it.key
        def value = it.value
        def tmp = value.split('/')
        def suiteName = tmp[tmp.size() - 1]
        def pytest_count_list = getPytestCollectedItems(value).split("\n")
        if(pytest_count_list.contains('0 selected')){
            println("No *${params.TESTTYPE.toLowerCase()}* test cases found in ${value}")
        }else{
            parallelSteps.put(suiteName, prepareOneBuildStage(suiteName, value))
        }
      }
  }else{
      def execute_failed_tcs = params.EXECUTE_FAILED_TCS
      if(execute_failed_tcs){
        def failed_tests_props = readProperties file: failedTestPropertiesFileInJenkins
        def failed_test_list = failed_tests_props['failed_tcs']

        def testCaseList = failed_test_list.split(' ')

        for(def key in testCaseList){
          def tmp = key.replace('.py', '').split('/')
          def suiteName = tmp[tmp.size() - 1].split('_').join(' ')
          parallelSteps.put(suiteName, prepareOneBuildStage(suiteName, key))
        }
      }else{
        for(def key in testcaseList){
          def tmp = key.split('/')
          def suiteName = tmp[tmp.size() - 1]
          def pytest_count_list = getPytestCollectedItems(key).split("\n")

          if(pytest_count_list.contains('0 selected')){
              println("No *${params.TESTTYPE.toLowerCase()}* test cases found in ${key}")
          }else{
            parallelSteps.put(suiteName, prepareOneBuildStage(suiteName, key))
          }
        }
      }
    }

    return parallelSteps
  }


  def prepareOneBuildStage(String name, String file) {
    return {
        stage("Test: ${name}") {
            def EXECUTE_SKIPPED = params.EXECUTE_SKIPPED_TCS
            if(params.EXECUTE_SKIPPED_TCS != 'yes'){
                EXECUTE_SKIPPED = 'no'
            }

            def PARALLEL_DEVICES = params.PARALLEL_DEVICES ? '--parallel-devices' : ''
            def DEVICE_LIST = params.DEVICE_LIST ? "--device-list=${params.DEVICE_LIST}" : ''

            if(params.EXECUTE_FAILED_TCS){
                def failedTestProperties = readProperties  file: failedTestPropertiesFileInJenkins
                ENV = failedTestProperties['env']
                TEST_URL = failedTestProperties['url']
                TESTTYPE = failedTestProperties['testtype']
                EXECUTE_SKIPPED_TCS = failedTestProperties['run_skipped']
                sh """
                    set +x
                    . ~/.axgo_profile
                    rm -rf ${WORKSPACE}/allure-results ${WORKSPACE}/testResults/ && python3 -m pytest --env=${ENV} ${file} -m ${params.TESTTYPE.toLowerCase()} --run-skipped=${EXECUTE_SKIPPED_TCS} --check-complaints=${params.CHECK_COMPLAINTS} --junitxml=${WORKSPACE}/testResults/${file}.xml --browser-version=${params.BROWSER_VERSION} --platform-name=${params.PLATFORM_NAME} --device-name="${params.DEVICE_NAME}" --device-os-version=${params.DEVICE_OS_VERSION} --enable-jenkins=yes --default-dataset=${params.DEFAULT_DATASET} --alluredir=${WORKSPACE}/allure-results -rA ${PARALLEL_DEVICES} ${DEVICE_LIST}
                    set -x
                """
            } else {
                if(jobUserId == 'timer'){
                    sh """
                        set +x
                        . ~/.axgo_profile
                        rm -rf ${WORKSPACE}/allure-results ${WORKSPACE}/testResults/ && python3 -m pytest --env=staging ${file} -m ${params.TESTTYPE.toLowerCase()} --run-skipped=${EXECUTE_SKIPPED} --check-complaints=${params.CHECK_COMPLAINTS} --junitxml=${WORKSPACE}/testResults/${file}.xml --browser-version=${params.BROWSER_VERSION} --platform-name=${params.PLATFORM_NAME} --device-name="${params.DEVICE_NAME}" --device-os-version=${params.DEVICE_OS_VERSION} --enable-jenkins=yes --default-dataset=${params.DEFAULT_DATASET} --alluredir=${WORKSPACE}/allure-results -rA ${PARALLEL_DEVICES} ${DEVICE_LIST}
                        set -x
                    """
                } else {
                    if(params.TEST_URL == ''){
                        sh """
                            set +x
                            . ~/.axgo_profile
                            rm -rf ${WORKSPACE}/allure-results ${WORKSPACE}/testResults/ && python3 -m pytest --env=${params.ENV.toLowerCase()} ${file} -m ${params.TESTTYPE.toLowerCase()} --run-skipped=${EXECUTE_SKIPPED} --check-complaints=${params.CHECK_COMPLAINTS} --junitxml=${WORKSPACE}/testResults/${file}.xml --browser-version=${params.BROWSER_VERSION} --platform-name=${params.PLATFORM_NAME} --device-name="${params.DEVICE_NAME}" --device-os-version=${params.DEVICE_OS_VERSION} --enable-jenkins=yes --default-dataset=${params.DEFAULT_DATASET} --alluredir=${WORKSPACE}/allure-results -rA ${PARALLEL_DEVICES} ${DEVICE_LIST}
                            set -x
                        """
                    } else {
                        sh """
                            set +x
                            . ~/.axgo_profile
                            rm -rf ${WORKSPACE}/allure-results ${WORKSPACE}/testResults/ && python3 -m pytest --env=${params.ENV.toLowerCase()} --url=${params.TEST_URL} ${file} -m ${params.TESTTYPE.toLowerCase()} --run-skipped=${EXECUTE_SKIPPED} --check-complaints=${params.CHECK_COMPLAINTS} --junitxml=${WORKSPACE}/testResults/${file}.xml --browser-version=${params.BROWSER_VERSION} --platform-name=${params.PLATFORM_NAME} --device-name="${params.DEVICE_NAME}" --device-os-version=${params.DEVICE_OS_VERSION} --enable-jenkins=yes --default-dataset=${params.DEFAULT_DATASET} --alluredir=${WORKSPACE}/allure-results -rA ${PARALLEL_DEVICES} ${DEVICE_LIST}
                            set -x
                        """
                    }
                }
            }
        }
    }
}