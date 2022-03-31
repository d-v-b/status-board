from matplotlib.axes import Axes
from matplotlib.figure import Figure
from status_board.models import Board, TaskType
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

y_buffer = 0
x_buffer = 0

colormap = {'Done': '#4285F4',
            'Planning': '#EA4335',
            'Waiting': '#FF6D01',
            'Queuing': '#FBBC04',
            'Progressing': '#34A853',
            'N/A' : '#D9D9D9'}
from status_board.generate_test_board import board

def draw_arrows(Tasks, row, axis):
    tdict = Tasks.dict()
    origin = (-.5, row)
    for idx, value in enumerate(tdict.values()):
        start = (origin[0] + idx, origin[1])
        color = colormap[value.status]
        arrow = mpatches.FancyArrow(*start, 1, 0, length_includes_head=True, width=.1, color=color)
        axis.add_patch(arrow)

def draw_circles(tdict, row, axis):
    origin = (0, row)
    for idx, value in enumerate(tdict.values()):
        start = (origin[0] + idx, origin[1])
        color = colormap[value.status]
        duration = value.duration_weeks
        patch = mpatches.Circle(start, .2, color=color, transform=axis.transData)
        axis.add_patch(patch)
        if value.status != 'N/A':
            axis.text(*start, duration, ha='center', va='center')


def plot_board(board: Board) -> Figure:
    projects = list(reversed(board.projects))
    num_rows = len(projects)
    num_cols = len(TaskType)
    fig = plt.figure(figsize=(x_buffer + num_cols, y_buffer + num_rows))
    axis = fig.add_axes((.2,.2,.9,.9))
    axis.axis('equal')
    #fig, axis = plt.subplots(figsize=(x_buffer + num_cols, y_buffer + num_rows))
    #axis.set_position((.5,.5,num_cols / (num_rows + num_cols), num_rows / (num_rows + num_cols)))
    axis.spines['bottom'].set_visible(False)
    axis.spines['right'].set_visible(False)
    axis.xaxis.set_ticks_position('top')
    xticklabels = [r.value for r in TaskType]
    yticklabels = [p.name for p in projects]
    axis.set_xlim(-.5, num_cols - .5)
    axis.set_ylim((-.5), ((num_rows-1) + .5))
    axis.set_xticks(range(num_cols))
    axis.set_yticks(range(num_rows))
    axis.set_yticklabels(yticklabels)
    axis.set_xticklabels(xticklabels, rotation=-45, ha='right')
    [axis.axvline(x-.5, color='gray', alpha=.3) for x in range(1,len(xticklabels))]

    for idx, project in enumerate(projects):
        draw_circles(project.tasks.dict(), idx, axis)

    # legend
    legend_size = .4
    ax_legend = fig.add_axes((.1,.1,legend_size, (legend_size / len(colormap))))
    ax_legend.set_xlim(-.5, len(colormap) - .5)
    #ax_legend.set_ylim(-.5, 1.5)
    ax_legend.set_xticks(range(len(colormap)))
    ax_legend.set_xticklabels(tuple(colormap.keys()), rotation=90, ha='right')
    ax_legend.spines['top'].set_visible(False)
    ax_legend.spines['left'].set_visible(False)
    ax_legend.spines['right'].set_visible(False)
    ax_legend.set_yticks([])
    ax_legend.axis('equal')
    origin = (0, 0)
    for idx, color in enumerate(colormap.values()):
        start = (origin[0] + idx, origin[1])
        patch = mpatches.Circle(start, .2, color=color, transform=ax_legend.transData)
        ax_legend.add_patch(patch)

    return fig

def main():
    fig = plot_board(board)
    #plt.tight_layout()
    plt.savefig('tmp.svg')

if __name__ == '__main__':
    main()
    