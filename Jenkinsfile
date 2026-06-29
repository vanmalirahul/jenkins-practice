pipeline {
    agent any

    environment {
        ANSIBLE_HOST_KEY_CHECKING = 'False'
    }

    stages {

        stage('Checkout Code') {
            steps {
                echo '📥 Pulling code from GitHub...'
                git branch: 'main',
                    url: 'https://github.com/vanmalirahul/jenkins-practice.git'
            }
        }

        stage('Validate Playbook') {
            steps {
                echo '🔍 Checking playbook for errors...'
                sh 'ansible-playbook playbooks/nginx.yaml --syntax-check'
            }
        }

        stage('Deploy') {
            steps {
                echo '🚀 Running playbook on target server...'
                ansiblePlaybook(
                    playbook: 'playbooks/nginx.yaml',
                    inventory: 'environments/dev/inventory',
                    credentialsId: 'ansible-ssh-key',
                    become: true
                )
            }
        }
    }

    post {
        success {
            echo '✅ Nginx installed successfully!'
        }
        failure {
            echo '❌ Something went wrong!'
        }
    }
}
