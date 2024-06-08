# ATENTION!! 
Pyrogram 2.0.106
BUG:
    raise ValueError(f"Peer id invalid: {peer_id}")
    ValueError: Peer id invalid: -1002185579056

Monckey fix:

File "D:\Doccuments\VSCode\VideoDownloadBot\env\Lib\site-packages\pyrogram\utils.py", line 246, in get_peer_type

replace metod with:

def get_peer_type(peer_id: int) -> str:
    peer_id_str = str(peer_id)
    if not peer_id_str.startswith("-"):
        return "user"
    elif peer_id_str.startswith("-100"):
        return "channel"
    else:
        return "chat"
