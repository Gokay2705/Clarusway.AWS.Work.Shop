### Simple Notification Service

### Part 1.

1. Amazon SNS servisini ac.
   1. Topics
   2. Create Topics
   3. Name:Demo-SNS
      1. Display name - optional:First-SNS
      2. Digerlerini "default" birak.
      3. Create Topic
    4. Create subscription
    5. Topic ARN	:default
    6. Protocol	:Email
    7. Create subscription
	
	Email hesabiniza gelen maili onaylayin. Spam icini kontrol edin.
	
	8. Subscriptions
   	
	   Bu menuden  Pending confirmation --->>> Confirmed oldugunu gorun.

2. Topics
   1. Publish message
      1. Subject: Konu adini yazin
      2. Message body: default
      3. Message body to send to the endpoint: Buraya mesaji yazin.
      4. Publish message
	
	Email hesabiniza mail gelecektir.

### Part 2.

1. Cloud Watch Menusune gir.
2. Event Type/Events/Rules
   1. Create rule

	2. Service Name: ec2
	3. Event Type: ec2 instance state-change notification
	4. Targets/SNS Topic
	5. Configure
      1. Name:EC2-State_Change
      2. Create Rule
	
3. EC2 menusune git bir instance stop et veya calistir.
   Bize mail gelecektir.
   
### Simple Queue Service

### Part 3.

1. Simple Queue Service girin.
   1. Queues
      1. Create queue
         1. Standard /FIFO	: Standard
         2. Name 			: Firts-SQS
         3. Configuration	: default
         4. Access Policy	: Basic secili default olacak
         5. Encryption 		:default
         6. Dead-letter queue 	: Disabled.	# Gonderenin msg alici lamaz ise Queue icinde kalir ve bu isler burada birikir.
       2. Create queue

2. Send and receive messages
   1. Message body	: First msg of SQS.
   2. Send message 
	
	Receive messages  bolumunde Messages available 1 oldugunu gor.

3. Poll for message tikla.
4. Mesaji sec ve Delete tikla.

### Part 4.

1. Lamda sevisine git
   1. AWS Lambda
   2. Create function
   3. Use BluePrint
   4. Blueprints	:SQS
   5. sqs-poller sec.
   6. configure
      1. Function name	:lamda_funk
      2. Role name: SQS-role
      3. SQS trigger
      4. Enable trigger sec.
      5. create function

2. Lamda menusunden Functions
   1. Lamda fonk sec
   2. Test tikla

3. SQS munusunden msj yolla tekrardan.
   1. Messages available kisminda onceki gibi 1 yamiyor?
   2. CloudWatch
      1. CloudWatch Logs
      2. Log groups
      3. /aws/lambda/lamda_funk tiklayin burada islemlerin lamda fonk tarafindan yapildigini gorebilirsiniz.

### Temizlik

1. Instance
2. SQS
3. SNS
   1. Subscriptions
   2. Topics
4. CloudWatch
   1. Delete log group(s)
   2. Rules
5. **Lamda**
