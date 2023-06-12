from peaceful_pie.unity_comms import UnityComms
import argparse

def run(args: argparse.Namespace) -> None:
    unity_comms = UnityComms(port=args.port)
    unity_comms.ResetPosition_Plane()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=9000)
    args = parser.parse_args()
    run(args)
