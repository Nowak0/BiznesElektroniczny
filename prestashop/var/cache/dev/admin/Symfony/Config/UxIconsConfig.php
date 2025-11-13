<?php

namespace Symfony\Config;

require_once __DIR__.\DIRECTORY_SEPARATOR.'UxIcons'.\DIRECTORY_SEPARATOR.'IconSetsConfig.php';
require_once __DIR__.\DIRECTORY_SEPARATOR.'UxIcons'.\DIRECTORY_SEPARATOR.'IconifyConfig.php';

use Symfony\Component\Config\Loader\ParamConfigurator;
use Symfony\Component\Config\Definition\Exception\InvalidConfigurationException;

/**
 * This class is automatically generated to help in creating a config.
 */
class UxIconsConfig implements \Symfony\Component\Config\Builder\ConfigBuilderInterface
{
    private $iconDir;
    private $defaultIconAttributes;
    private $iconSets;
    private $aliases;
    private $iconify;
    private $ignoreNotFound;
    private $_usedProperties = [];

    /**
     * The local directory where icons are stored.
     * @default '%kernel.project_dir%/assets/icons'
     * @param ParamConfigurator|mixed $value
     * @return $this
     */
    public function iconDir($value): static
    {
        $this->_usedProperties['iconDir'] = true;
        $this->iconDir = $value;

        return $this;
    }

    /**
     * Default attributes to add to all icons.
     * @example icon
     * @default array (
     *   'fill' => 'currentColor',
     * )
     * @param ParamConfigurator|mixed $value
     *
     * @return $this
     */
    public function defaultIconAttributes(mixed $value = array (
      'fill' => 'currentColor',
    )): static
    {
        $this->_usedProperties['defaultIconAttributes'] = true;
        $this->defaultIconAttributes = $value;

        return $this;
    }

    /**
     * Icon sets configuration.
    */
    public function iconSets(string $prefix, array $value = []): \Symfony\Config\UxIcons\IconSetsConfig
    {
        if (!isset($this->iconSets[$prefix])) {
            $this->_usedProperties['iconSets'] = true;
            $this->iconSets[$prefix] = new \Symfony\Config\UxIcons\IconSetsConfig($value);
        } elseif (1 < \func_num_args()) {
            throw new InvalidConfigurationException('The node created by "iconSets()" has already been initialized. You cannot pass values the second time you call iconSets().');
        }

        return $this->iconSets[$prefix];
    }

    /**
     * @param ParamConfigurator|list<ParamConfigurator|mixed> $value
     *
     * @return $this
     */
    public function aliases(ParamConfigurator|array $value): static
    {
        $this->_usedProperties['aliases'] = true;
        $this->aliases = $value;

        return $this;
    }

    /**
     * Configuration for the remote icon service.
     * @default {"enabled":true,"on_demand":true,"endpoint":"https:\/\/api.iconify.design"}
    */
    public function iconify(array $value = []): \Symfony\Config\UxIcons\IconifyConfig
    {
        if (null === $this->iconify) {
            $this->_usedProperties['iconify'] = true;
            $this->iconify = new \Symfony\Config\UxIcons\IconifyConfig($value);
        } elseif (0 < \func_num_args()) {
            throw new InvalidConfigurationException('The node created by "iconify()" has already been initialized. You cannot pass values the second time you call iconify().');
        }

        return $this->iconify;
    }

    /**
     * Ignore error when an icon is not found.
     * Set to 'true' to fail silently.
     * @default false
     * @param ParamConfigurator|bool $value
     * @return $this
     */
    public function ignoreNotFound($value): static
    {
        $this->_usedProperties['ignoreNotFound'] = true;
        $this->ignoreNotFound = $value;

        return $this;
    }

    public function getExtensionAlias(): string
    {
        return 'ux_icons';
    }

    public function __construct(array $value = [])
    {
        if (array_key_exists('icon_dir', $value)) {
            $this->_usedProperties['iconDir'] = true;
            $this->iconDir = $value['icon_dir'];
            unset($value['icon_dir']);
        }

        if (array_key_exists('default_icon_attributes', $value)) {
            $this->_usedProperties['defaultIconAttributes'] = true;
            $this->defaultIconAttributes = $value['default_icon_attributes'];
            unset($value['default_icon_attributes']);
        }

        if (array_key_exists('icon_sets', $value)) {
            $this->_usedProperties['iconSets'] = true;
            $this->iconSets = array_map(fn ($v) => new \Symfony\Config\UxIcons\IconSetsConfig($v), $value['icon_sets']);
            unset($value['icon_sets']);
        }

        if (array_key_exists('aliases', $value)) {
            $this->_usedProperties['aliases'] = true;
            $this->aliases = $value['aliases'];
            unset($value['aliases']);
        }

        if (array_key_exists('iconify', $value)) {
            $this->_usedProperties['iconify'] = true;
            $this->iconify = new \Symfony\Config\UxIcons\IconifyConfig($value['iconify']);
            unset($value['iconify']);
        }

        if (array_key_exists('ignore_not_found', $value)) {
            $this->_usedProperties['ignoreNotFound'] = true;
            $this->ignoreNotFound = $value['ignore_not_found'];
            unset($value['ignore_not_found']);
        }

        if ([] !== $value) {
            throw new InvalidConfigurationException(sprintf('The following keys are not supported by "%s": ', __CLASS__).implode(', ', array_keys($value)));
        }
    }

    public function toArray(): array
    {
        $output = [];
        if (isset($this->_usedProperties['iconDir'])) {
            $output['icon_dir'] = $this->iconDir;
        }
        if (isset($this->_usedProperties['defaultIconAttributes'])) {
            $output['default_icon_attributes'] = $this->defaultIconAttributes;
        }
        if (isset($this->_usedProperties['iconSets'])) {
            $output['icon_sets'] = array_map(fn ($v) => $v->toArray(), $this->iconSets);
        }
        if (isset($this->_usedProperties['aliases'])) {
            $output['aliases'] = $this->aliases;
        }
        if (isset($this->_usedProperties['iconify'])) {
            $output['iconify'] = $this->iconify->toArray();
        }
        if (isset($this->_usedProperties['ignoreNotFound'])) {
            $output['ignore_not_found'] = $this->ignoreNotFound;
        }

        return $output;
    }

}
