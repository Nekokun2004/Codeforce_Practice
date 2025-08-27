print("? ", x, k, *S, flush=True)  

import sys
sys.stdout.write(f"? {x} {k} " + " ".join(map(str, S)) + "\n")
sys.stdout.flush()
