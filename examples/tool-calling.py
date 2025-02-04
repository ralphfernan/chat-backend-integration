#@tool(response_format="content_and_artifact") requires a 2-tuple of message content and raw tool output.
@tool
def validate_user(user_id: str, addresses: List[str]) -> bool:
    """Validate user using historical addresses.

    Args:
        user_id (int): the user ID.
        addresses (List[str]): Previous addresses as a list of strings.
    """
    res = False
    valid_userid = 'moz'
    valid_addresses = {'123 Fake St, Boston, MA','456 Somewhere St, Tokyo, JP'}
    match (user_id, addresses):
        case valid_userid,_ if valid_addresses & set(addresses):
            res = True
        case _:
            res = False
    return res


llm = ChatOllama(
    model="mistral-small",
    temperature=0,
).bind_tools([validate_user])

prompt = """
Please validate user moz.  
He previously lived at the following places:
123 Fake St in Boston MA
456 Somewhere St, Tokyo, JP
"""
result = llm.invoke(prompt)
result.tool_calls

name = None
args = None
res = None
if result and result.tool_calls:
    tools_called = result.tool_calls
    if 'name' in tools_called[0]:
        name = tools_called[0]['name']
        args = tools_called[0]['args']
        print(f"Calling function {name}")
        # instead of this pattern, can also use a dict of names to functions.
        match name, args:
          case 'validate_user', args:
              res = validate_user.invoke(args)
          case _:
              res = False

print(f"Got result of tool-call: {res}")

print(f"Got result of tool-call: {res}")