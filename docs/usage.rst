Usage
=====

.. rst:directive:: .. platform-picker::

The ``platform-picker`` directive defines a platform-specific block. In this block, a single platform is chosen to be visible at any time. The available platforms are rendered as buttons that can be clicked to switch the visible platform.

.. rst:directive:: .. platform-choice:: name

The ``platform-choice`` directive defines the content for a single platform. Each directive must specify a ``name`` argument, unique in the ``platform-picker`` block. The text on the corresponding button is set by the ``title`` option. The ``altname`` option sets a more generic name for a platform, so that some platform-specific blocks can be more detailed than others.

For example:

.. code-block:: rst

    .. platform-picker::

        .. platform-choice:: windows
            :title: Windows

            Instructions for Windows

        .. platform-choice:: macos
            :title: macOS

            Instructions for macOS

        .. platform-choice:: linux
            :title: Linux

            Instructions for Linux

will be rendered as:

.. platform-picker::

    .. platform-choice:: windows
        :title: Windows

        Instructions for Windows

    .. platform-choice:: macos
        :title: macOS

        Instructions for macOS

    .. platform-choice:: linux
        :title: Linux

        Instructions for Linux

The ``platform-picker`` directive can be specified many times on a single page, and all of them will switch at the same time:

.. platform-picker::

    .. platform-choice:: windows
        :title: Windows

        More instructions for Windows

    .. platform-choice:: macos
        :title: macOS

        More instructions for macOS

    .. platform-choice:: linux
        :title: Linux

        More instructions for Linux

The ``altname`` option can be used to drill down into a single platform in one of the sections but not others. If there is a choice with a certain ``altname`` and a choice with the same ``name``, the latter is preferred. For example:

.. code-block:: rst

    .. platform-picker::

        .. platform-choice:: windows
            :title: Windows

            Instructions for Windows

        .. platform-choice:: macos
            :title: macOS

            Instructions for macOS

        .. platform-choice:: debian
            :title: Debian Linux
            :altname: linux

            Specific instructions for Debian Linux

        .. platform-choice:: arch
            :title: Arch Linux
            :altname: linux

            Specific instructions for Arch Linux

        .. platform-choice:: linux
            :title: Other Linux

            Generic instructions for any Linux

Consider how the following two blocks interact with each other:

.. platform-picker::

    .. platform-choice:: windows
        :title: Windows

        Instructions for Windows

    .. platform-choice:: macos
        :title: macOS

        Instructions for macOS

    .. platform-choice:: debian
        :title: Debian Linux
        :altname: linux

        Specific instructions for Debian Linux

    .. platform-choice:: arch
        :title: Arch Linux
        :altname: linux

        Specific instructions for Arch Linux

    .. platform-choice:: linux
        :title: Other Linux

        Generic instructions for any Linux

.. platform-picker::

    .. platform-choice:: windows
        :title: Windows

        More instructions for Windows

    .. platform-choice:: macos
        :title: macOS

        More instructions for macOS

    .. platform-choice:: linux
        :title: Linux

        More generic instructions for all Linuxes
