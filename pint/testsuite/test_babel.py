import os

import pytest

from pint import UnitRegistry
from pint.testsuite import helpers


@helpers.requires_not_babel()
def test_no_babel(func_registry):
    ureg = func_registry
    distance = 24.0 * ureg.meter
    with pytest.raises(Exception):
        distance.format_babel(locale="fr_FR", length="long")


@helpers.requires_babel()
def test_format(func_registry):
    ureg = func_registry
    dirname = os.path.dirname(__file__)
    ureg.load_definitions(os.path.join(dirname, "../xtranslated.txt"))

    distance = 24.0 * ureg.meter
    assert distance.format_babel(locale="fr_FR", length="long") == "24.0 mètres"
    time = 8.0 * ureg.second
    assert time.format_babel(locale="fr_FR", length="long") == "8.0 secondes"
    assert time.format_babel(locale="ro", length="short") == "8.0 s"
    acceleration = distance / time**2
    assert (
        acceleration.format_babel(locale="fr_FR", length="long")
        == "0.375 mètre par seconde²"
    )
    mks = ureg.get_system("mks")
    assert mks.format_babel(locale="fr_FR") == "métrique"


@helpers.requires_babel()
def test_registry_locale():
    ureg = UnitRegistry(fmt_locale="fr_FR")
    dirname = os.path.dirname(__file__)
    ureg.load_definitions(os.path.join(dirname, "../xtranslated.txt"))

    distance = 24.0 * ureg.meter
    assert distance.format_babel(length="long") == "24.0 mètres"
    time = 8.0 * ureg.second
    assert time.format_babel(length="long") == "8.0 secondes"
    assert time.format_babel(locale="ro", length="short") == "8.0 s"
    acceleration = distance / time**2
    assert acceleration.format_babel(length="long") == "0.375 mètre par seconde²"
    mks = ureg.get_system("mks")
    assert mks.format_babel(locale="fr_FR") == "métrique"


@helpers.requires_babel()
def test_unit_format_babel():
    ureg = UnitRegistry(fmt_locale="fr_FR")
    volume = ureg.Unit("ml")
    assert volume.format_babel() == "millilitre"

    ureg.default_format = "~"
    assert volume.format_babel() == "ml"

    dimensionless_unit = ureg.Unit("")
    assert dimensionless_unit.format_babel() == ""

    ureg.set_fmt_locale(None)
    with pytest.raises(ValueError):
        volume.format_babel()


@helpers.requires_babel()
def test_no_registry_locale(func_registry):
    ureg = func_registry
    distance = 24.0 * ureg.meter
    with pytest.raises(Exception):
        distance.format_babel()


@helpers.requires_babel()
def test_str(func_registry):
    ureg = func_registry
    d = 24.0 * ureg.meter

    s = "24.0 meter"
    assert str(d) == s
    assert "%s" % d == s
    assert f"{d}" == s

    ureg.set_fmt_locale("fr_FR")
    s = "24.0 mètres"
    assert str(d) == s
    assert "%s" % d == s
    assert f"{d}" == s

    ureg.set_fmt_locale(None)
    s = "24.0 meter"
    assert str(d) == s
    assert "%s" % d == s
    assert f"{d}" == s
