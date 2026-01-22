import pytest
from open_aglabs.core.base_models import Location, TrialProperties
from open_aglabs.plot_book.models import PlotBook, PlotEntry


def test_plotbook_initialization_with_defaults():
    plotbook = PlotBook()
    assert isinstance(plotbook.plotbook_id, str)
    assert len(plotbook.plotbook_id) > 0
    assert plotbook.entries == []
    assert plotbook.location_properties is None
    assert plotbook.trial_properties is None


def test_plotbook_initialization_with_data():
    location = Location(id="loc1")
    trial = TrialProperties(id="trial1")
    entry = PlotEntry(
        plot_id="plot1",
        observation_unit_name="unit1",
        plot_number=1,
        row=2,
        column=3,
        replicate=1
    )
    plotbook = PlotBook(
        entries=[entry],
        location_properties=location,
        trial_properties=trial
    )
    assert len(plotbook.entries) == 1
    assert plotbook.entries[0].plot_id == "plot1"
    assert plotbook.location_properties.id == "loc1"
    assert plotbook.trial_properties.id == "trial1"


def test_plotentry_creation():
    entry = PlotEntry(
        plot_id="entry1",
        observation_unit_name="unit1",
        plot_number=5,
        row=1,
        column=2,
        replicate=2,
        plot_name="Plot Name",
        germplasm_name="Germplasm A",
        block_number=1
    )
    assert entry.plot_id == "entry1"
    assert entry.observation_unit_name == "unit1"
    assert entry.plot_number == 5
    assert entry.row == 1
    assert entry.column == 2
    assert entry.replicate == 2
    assert entry.plot_name == "Plot Name"
    assert entry.germplasm_name == "Germplasm A"
    assert entry.block_number == 1


def test_plotbook_empty_entries():
    plotbook = PlotBook(entries=[])
    assert plotbook.entries == []


def test_plotentry_optional_fields():
    entry = PlotEntry(
        plot_id="entry2",
        observation_unit_name="unit2",
        plot_number=10,
        row=4,
        column=5,
        replicate=3
    )
    assert entry.plot_name is None
    assert entry.germplasm_name is None
    assert entry.block_number is None
