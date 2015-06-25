import zn_api
from deploy import deploy
from wg_util import plugin_context_message
from wg_util import api_response_message
from wg_util import query_yes_no

def prompt_publish(context):

	question = plugin_context_message("Publish", context) + "?"

	should_publish = query_yes_no(question)

	if should_publish:
		publish(context)

def publish(context):

	deploy(context)

	print plugin_context_message("Publishing", context)

	response = zn_api.publish(context)

	print api_response_message(response)