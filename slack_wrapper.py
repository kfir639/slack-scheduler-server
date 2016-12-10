from slacker import Slacker

class SlackWrapper:
	
	def __init__(self, auth_token):
		self.slack = Slacker(auth_token)
		
	def send_direct_message_to_all_users(self, message):
		all_users = self.slack.users.list().body["members"]
		for user in all_users:
			self.slack.chat.post_message(user["id"], message, as_user=True)
		