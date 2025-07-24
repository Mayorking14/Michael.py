print("""
 WELCOME TO NOKIA 
Main menu:
  	1-> Phone book 
  	2-> Message
  	3-> Chat
  	4-> Call register
  	5-> Tones
  	6-> Settings
  	7-> Call divert
  	8-> Games
  	9-> Calculator
  	10-> Reminders
  	11-> Clock
  	12-> Profiles
  	13-> SIM services
	""")

userinput = int(input('Select any option:\n'))
match userinput:
	case 1: 
		print("""
  		1. Search
  		2. Service Nos
  		3. Add name
  		4. Erase 
  		5. Edit
  		6. Assign tone
  		7. Send b'card
  		8. Option
  		9. Speed dials
  		10. Voice tags 
		""")
		phonebook = int(input('Enter option:'))
		match phonebook :
			case 1: 
				print('Search')
			case 2: 
				print('Service Nos')
			case 3: 
				print('Add name')
			case 4: 
				print('Erase')
			case 5: 
				print('Edit')
			case 6: 
				print('Assign tone')
			case 7: 
				print('Send b card')
			case 8:
				print(""" 
				1-> Type of view
				2-> Memory status
				""")
				view_status = int(input("Select 1 or 2 :"))
				match view_status :
					case 1: print('Type of view')
					case 2: print('Memory status')
			
			case 9: 
				print('Speed dials')
			case 10: 
				print('Voice tags')
	case 2:
		print("""
		1. Write messages
  		2. Inbox 
  		3. Outbox
  		4. Picture messages
  		5. Templates
  		6. Smileys
  		7. Message settings
  		8. Info services
  		9. Voice mailbox number
  		10. Service command editor
  		""")
		message = int(input('Enter option to proceed:\n'))
		match message:
			case 1:
				print('Write messages')
			case 2:
				print('Inbox')
			case 3:
				print('Outbox')
			case 4:
				print('Picture messages')
			case 5:
				print('Templates')
			case 6:
				print('Smileys')
			case 7:
				print(""" 
				1. Set
				2. Common
				""")
				message_settings = int(input('message_settings:'))
				match message_settings:
					case 1:
						print("""
						1. Message center number
						2. Message sent as
						3. Message validity
						""")
						set = int(input('Enter option: '))
						match set: 
							case 1:
								print('Message center number')
							case 2:
								print('Message sent as')
							case 3:
								print('Message validity')

							case (_):
								print('invalid')
					case 2:
						print("""
						1. Delivery reports
						2. Reply via same centre
						3. Character support
						""")
						common = int(input('Enter option:'))
						match common: 
							case 1:
								print('Delivery reports')
							case 2:
								print('Reply via same centre')
							case 3:
								print('Character supports')

							case (_):
								print('invalid')

			case 8:
				print('Info services')
			case 9:
				print('Voice mailbox number')
			case 10:
				print('Service command editor')
			case (_):
				print('invalid')
	case 3:
		print("""
		chat
		""")
	case 4:
		print("""
		1.Missed calls
		2.Received calls
		3.Dialled numbers
		4.Dialled call's duration
		5.Show call duration
		6.Show call cost
		7.Call cost settings
		8.Prepaid credit
		""")
		register = int(input('Enter option to proceed:'))
		match register:
				case 1:
					print('Missed calls')
				case 2:
					print('Received calls')
				case 3:
					print('Dialled numbers')
				case 4:
					print('Dialled calls duration')
				case 5:
					print("""
					1. Last call duration
					2. All calls duration
					3. Received calls duration
					4. Dialled calls duration
					""")
					duration = int(input('Select any option :'))
					match duration:
						case 1:
							print('Last call duration')
						case 2:
							print('All calls duration')
						case 3:
							print('Received calls duration')
						case 4:
							print('Dialled calls duration')
						case (_):
							print('invalid')
				case 6:
					print("""
					1. Last call cost
					2. All call cost
					3. Clear counters
					""")
					call_cost =  int(input('Select any option :'))
					match call_cost: 
						case 1:
							print('Last call cost')
						case 2:
							print('All call cost')
						case 3:
							print('Clear counters')
						case (_):
							print('invalid')
				case 7:
					print("""
					1. Call cost limit
					2. Show call cost in
					""")
					callee =  int(input('Select option :'))
					match callee: 
						case 1:
							print('Call cost limit')
						case 2:
							print('Show call cost in')
						case (_):
							print('invalid')
				case 8:
					print("""
					prepaid credit
					""")
				case (_):
					print('invalid')
	case 5:
		print("""
		1. Ringing tone
 		2. Ringing volume
 		3. Incoming call alert
 		4. Composer
 		5. Message alert tone
 		6. Warning and game tones
 		7. Vibrating alert
		8. Screen saver 
		""")
		tones = int(input('Enter any option:'))
		match tones:
				case 1:
					print('Ringing tone')
				case 2:
					print('Ringing volume')
				case 3:
					print('Incoming call alert')
				case 4:
					print('Composer')				
				case 5:
					print('Message alert tone')
				case 6:
					print('Warning and game tones')
				case 7:
					print('Vibrating alert')
				case 8:
					print('Screen saver')
				case (_):
					print('Wrong input')
	case 6:
		print("""
		1. Call settings
		2. Phone settings
		3. Security settings
		4. Restore factory settings
		""")
		call_setting = int(input('Enter any option :'))
		match call_setting:
				case 1:
					print("""
					1.Automatic redial
					2.Speed dialing
					3.Call waiting option
					4.Own number sending
					5.Phone line in use
					6.Automatic answer
					""")
					call_setting1 = int(input('Enter any option:'))
					match call_setting1 :
							case 1:
								print('Automatic redial')
							case 2:
								print('Speed dialing')
							case 3:
								print('Call waiting option')
							case 4:
								print('Own number sending')
							case 5:
								print('Phone line in use')
							case 6:
								print('Automatic answer')
							case (_):
								print('invalid')
				case 2:
					print("""
					1.Language
					2.Cell info display
					3.Welcome note
					4.Network selection
					5.Light
					6.Confirm SIM service actions
					""")
					phone_setting = int(input('Enter any option:'))
					match phone_setting:
							case 1:
								print('Language')
							case 2:
								print('Cell info display')
							case 3:
								print('Welcome note')
							case 4:
								print('Network selection')
							case 5:
								print('Light')
							case 6:
								print('Confirm SIM service actions')
							case (_):
								print('invalid')

				case 3:
					print("""
					1.PIN code request
					2.Call barring service
					3.Fixed dialling
					4.Closed user group
					5.Phone security
					6.Change access codes
					""") 
					Security_settings =  int(input('Enter any option:'))
					match Security_settings:
							case 1:
								print('PIN code request')
							case 2:
								print('Call barring service')
							case 3:
								print('Fixed dialling')
							case 4:
								print('Closed user group')
							case 5:
								print('Phone security')
							case 6:
								print('Change access codes')
							case (_):
								print('Wrong input')
				case 4:
					print("""
					Restore factory settings
					""")
	case 7:
		print("""
		Call divert
		""")
	case 8:
		print("""
		Games
		""")
	case 9:
		print("""
		Calculator
		""")
	case 10:
		print("""
		Reminders
		""")
	case 11:
		print("""
		1. Alarm clock
		2. Clock settings
		3. Date setting
		4. Stopwatch
		5. Countdown timer
		6. Auto update of date and time
		""")
		alarm = int(input('Enter any option:'))
		match alarm:
				case 1:
					print('Alarm clock')
				case 2:
					print('Clock settings')
				case 3:
					print('Date setting')
				case 4:
					print('Stopwatch')
				case 5:
					print('Countdown timer')
				case 6:
					print('Auto update of date and time')
				case (_):
					print('invalid')
	case 12:
		print("""
		Profiles
		""")
	case 13:
		print("""
		SIM services
		""")
	case (_):
		print('invalid')
				