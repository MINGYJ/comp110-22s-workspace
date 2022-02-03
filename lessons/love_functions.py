"""..."""

def love(name: str) -> str:
    """Given a name as aparameter, returns a love string."""
    return f"I love you {name}!"

def spread_love(to:str, n:int) -> str:
    """Generate a string that repeats a loving message in times"""
    love_note: str=""
    count_times: int=0
    while(count_times < n):
        love_note += love(to)
        love_note += f"\n"
        count_times += 1
    return love_note



