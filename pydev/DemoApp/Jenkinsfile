pipeline {
    agent none

    stage("Get Code"){
			
			echo 'Pulling...' + env.BRANCH_NAME
		
		step("Get Code"){
			git branch: 'pybranch', credentialsId: '0c1cde73-5a15-4ac6-87ae-68a6dc233580', url: 'https://github.com/SAAMalusare/jenkinspipeline.git'
		}
	}
}