from util.plot_utils import plot_logs
from pathlib import Path
import argparse


def get_args_parser():
    parser = argparse.ArgumentParser(
        'Plotting logs', add_help=False)
    parser.add_argument('--output_dir', default='runs_scratch_MEAN_adam_ciou/', type=str)
    parser.add_argument('--save_dir',
                        default='charts/file.jpg', type=str)

    return parser


fields_of_interest = ('mAP', 'loss', 'class_error', 'loss_bbox', 'loss_ciou')


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        'Plotting logs', parents=[get_args_parser()])
    args = parser.parse_args()

    log_directory = [Path(args.output_dir)]
    plot_logs(log_directory, args.save_dir, fields=fields_of_interest)
